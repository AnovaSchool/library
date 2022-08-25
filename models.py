from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal
from math import ceil
from telnetlib import EC
import uuid
from dateutil import parser
from collections import Counter
from datetime import date
#####
@dataclass
class Person:
    name: str
    def __str__(self):
        
        return self.name

@dataclass
class Member(Person):
    def __str__(self):
        return self.name

@dataclass
class Employee(Person):
    pass

@dataclass
class Book:
    name: str
    isbn: str
    def __str__(self):
        return self.name

    # Just for show names.

@dataclass
class LendingTransaction:
    member: Member
    book: Book
    last_give_back_date: datetime.date
    id: str = str(uuid.uuid4())
    give_back_date: datetime.date = None
    borrow_date: datetime = datetime.utcnow()
    is_active: bool = True

@dataclass
class PaymentTransaction:
    member: Member
    amount: Decimal
    created_at: datetime = datetime.utcnow()
    is_active : bool = False

@dataclass
class Library:
    
    name: str
    default_lending_day: int 
    default_lending_count: int 
    daily_penalty_for_late_give_back: Decimal
    total_library_money: Decimal = 0
    members: list[Member] = field(default_factory=list)
    lending_transactions: list[LendingTransaction] = field(default_factory=list)
    payment_transactions: list[PaymentTransaction] = field(default_factory=list)
    books: list[Book] = field(default_factory=list)
    created_at: datetime = datetime.utcnow()
    
    def register_member(self, member: Member):

        if member in self.members:
            print("This user is already registered.")   ## This should be raise Exception but I'm trying so I wrote there print

        else:
            self.members.append(member)
            print(f"Member {member.name} is registered.")

    def show_members(self):
        for member in self.members:
            print(member)

    def register_book(self, book: Book):
        self.books.append(book)
    
    def register_lending(self, lending: LendingTransaction):
        if lending in self.lending_transactions:
            print("This transaction already done.")
        else:
            self.lending_transactions.append(lending)

    def active_book_list(self):
        # x = Counter(self.books)
        # a= [[x,self.books.count(x)] for x in set(self.books)]
        # biz bunu denedik de olmadı.
        i= 1
        for book in self.books:
            print(f"{i} : {book} ")
            i+= 1
            
    def give_back_book(self, member: Member, book: Book):
        active_lendings = filter(
            lambda transaction: transaction.member == member \
                and transaction.is_active == True \
                and transaction.book == book, 
            self.lending_transactions)
        if not active_lendings:
            raise Exception("This book is not yours.")

        penalty = self.find_member_penalty(member=member)
        if penalty:
            print("You have unpaid penalties. Please pay.")
        
        lending: LendingTransaction = active_lendings[0]
        lending.give_back_date = datetime.utcnow()
        lending.is_active = False

        for transaction in self.lending_transactions:
            if transaction.book == book and transaction.member == member and transaction.is_active == True:
                transaction = lending
        
    
    
    def lend_book(self, lending: LendingTransaction):

        if lending in self.lending_transactions:
            print("This transaction is already done.")
        else: 
            self.lending_transactions.append(lending)


        active_late_lendings = list(filter(
            lambda transaction: transaction.member == lending.member \
                and transaction.is_active == True \
                and datetime.utcnow() > transaction.last_give_back_date \
                and transaction.give_back_date is None,
            self.lending_transactions))
        
        if active_late_lendings:
            print(f'{lending.member.name}, {lending.book.name} You are late for some books. Please, give back them first.') 
        
        penalty = self.find_member_penalty(member=lending.member)
        
        if penalty:
            print("Pay your penalty.")

        active_lendings = list(filter(lambda transaction: transaction.member == lending.member and transaction.is_active == True, self.lending_transactions))
        # burada is_active = True olması gerekli mi ? 
        
        if len(active_lendings) >= self.default_lending_count:
            print("You have reached library book lending limit. Please, give back some of our books.")
        
        active_same_lendings = list(filter(lambda transaction: transaction.member == lending.member and transaction.book == lending.book and transaction.is_active == True, self.lending_transactions))
        if active_same_lendings:
            print("You have this book.")
            
        # Her türlü You have this book uyarısı alıyoruz . Bence lend book işlemi eğer yapılırsa is_active = False yapmamız gerekir. 
   
        self.lending_transactions.append(LendingTransaction(member=lending.member, book=lending.book, last_give_back_date=datetime.utcnow() + timedelta(days=self.default_lending_day)))
        # burası self.lending_transactions'ın doldurulduğu yer 


    ## giveback geri verdiğimiz kitap 
    ## lend book kütüphaneden aldığımız kitap 
    ## Alınan kitap book listten remove edilmeli. Ama kaç tane aynı kitaptan olduğunu saydıramıyoruz. #groupby kullan

    def find_member_penalty(self, member: LendingTransaction):
        late_lendings = list(filter(
            lambda transaction: transaction.member == member
            and transaction.give_back_date is not None 
            and transaction.last_give_back_date < transaction.give_back_date , 
            self.lending_transactions))
        #print(late_lendings)

        total_penalty = 0
        for transaction in late_lendings:
            total_penalty += (transaction.give_back_date-transaction.last_give_back_date).days * self.daily_penalty_for_late_give_back
            self.total_library_money += total_penalty
            if total_penalty != 0:
                print(f'{transaction.member}, You need to pay {ceil(total_penalty)} £')
                
        
        
        #total_penalty = ceil(sum((transaction.give_back_date - transaction.last_give_back_date).days for transaction in late_lendings)) * self.daily_penalty_for_late_give_back
        
        payments = list(filter(lambda transaction: transaction.member == member, self.payment_transactions))
        total_payment = sum(payment.amount for payment in payments)
        

        if total_payment < total_penalty:
            return total_penalty - total_payment
        return 0

    def giveback_book(self,member: Member, book: Book):
    
        active_giveback_books = filter(lambda transaction: transaction.member == member \
            and transaction.book == book \
            and transaction.is_active == False, self.lending_transactions)

        if active_giveback_books:
            self.lending_transactions.append(active_giveback_books)
            
    #     total_payment = sum(payment.amount for payment in self.payment_transactions)
    #     print(total_payment
    def all_library_money(self):
        print(f'Total Library Money: {self.total_library_money}')

    def payments(self, payment: PaymentTransaction):
        late_lendings = list(filter(
            lambda transaction: transaction.member == payment
            and transaction.give_back_date is not None 
            and transaction.last_give_back_date < transaction.give_back_date , 
            self.lending_transactions))
        #print(late_lendings)

        total_penalty = 0
         
        for transaction in late_lendings:
            total_penalty += (transaction.give_back_date-transaction.last_give_back_date).days * self.daily_penalty_for_late_give_back
            self.total_library_money += total_penalty
            

        
    
