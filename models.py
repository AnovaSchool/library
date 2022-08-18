from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal
from math import ceil
from telnetlib import EC
import uuid
from dateutil import parser

@dataclass
class Person:
    name: str

@dataclass
class Member(Person):
    pass

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
    last_give_back_date: datetime
    id: str = str(uuid.uuid4())
    give_back_date: datetime = None
    borrow_date: datetime = datetime.utcnow()
    is_active: bool = True

@dataclass
class PaymentTransaction:
    member: Member
    amount: Decimal
    created_at: datetime = datetime.utcnow()

@dataclass
class Library:
    name: str
    default_lending_day: int 
    default_lending_count: int 
    daily_penalty_for_late_give_back: Decimal
    members: list[Member] = field(default_factory=list)
    lending_transactions: list[LendingTransaction] = field(default_factory=list)
    payment_transactions: list[PaymentTransaction] = field(default_factory=list)
    books: list[Book] = field(default_factory=list)
    created_at: datetime = datetime.utcnow()
    
    def register_member(self, member: Member):

        if member in self.members:
            print("This user is already registered.")

        else:
            self.members.append(member)
            print(f"Member {member.name} is registered.")

    def show_members(self):
        print(f'{self.members}')
    
    def register_book(self, book: Book):
        self.books.append(book)
    
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
        


        
    def find_member_penalty(self, member: Member):
        late_lendings = filter(
            lambda transaction: transaction.member == member
            and transaction.give_back_date is not None 
            and transaction.last_give_back_date < transaction.give_back_date, 
            self.lending_transactions)

        total_penalty = 0
        for transaction in late_lendings:
            total_penalty += (transaction.give_back_date - transaction.last_give_back_date).days  * self.daily_penalty_for_late_give_back
        total_penalty = ceil(total_penalty)
        #total_penalty = ceil(sum((transaction.give_back_date - transaction.last_give_back_date).days for transaction in late_lendings)) * self.daily_penalty_for_late_give_back
        
        payments = filter(lambda transaction: transaction.member == member, self.payment_transactions)
        total_payment = sum(payment.amount for payment in payments) 

        if total_payment < total_penalty:
            return total_penalty - total_payment
        return 0
            
    
    def lend_book(self, member: Member, book: Book):
        # if user has late book
        active_late_lendings = filter(
            lambda transaction: transaction.member == member \
                and transaction.is_active == True \
                and transaction.last_give_back_date < datetime.utcnow(), 
            self.lending_transactions)

        if not active_late_lendings:
            print(f'{member.name}, {book.name} You are late for some books. Please, give back them first.') 
            ## If a person is unpaid he can't get any book from library. He can't have books.
            ## Bunu her türlü yazıyor. 
            # Unpaid penalties
        
        penalty = self.find_member_penalty(member=member)
        if penalty:
            print("Pay your penalty.")
        ## We used the same thing in def give_back_book we need to check it out. 

        active_lendings = list(filter(lambda transaction: transaction.member == member and transaction.is_active == True, self.lending_transactions))
        
        if len(active_lendings) >= self.default_lending_count:
            print("You have reached library book lending limit. Please, give back some of our books.")
        ## TypeError: object of type 'filter' has no len() ## aldığımız hata bu.

        active_same_lendings = list(filter(lambda transaction: transaction.member == member and transaction.book == book and transaction.is_active == True, self.lending_transactions))
        print(active_same_lendings)
        if active_same_lendings:
            print("You have this book.")
        
        
        self.lending_transactions.append(LendingTransaction(member=member, book=book, last_give_back_date=datetime.utcnow() + timedelta(days=self.default_lending_day)))


    def giveback_book(self,member: Member, book: Book):
    
        active_giveback_books = filter(lambda transaction: transaction.member == member \
            and transaction.book == book \
            and transaction.is_active == False, self.lending_transactions)

        if active_giveback_books:
            self.lending_transactions.append(active_giveback_books),
    
    def giveback_book_list(self):
        for book in self.books:
            print(book)
 ### FAST API OKU ARAŞTIR
 