from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal
from math import ceil
from telnetlib import EC
from typing import Optional


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

@dataclass
class LendingTransaction:
    member: Member
    book: Book
    give_back_date: datetime 
    is_active: bool
    last_give_back_date: datetime
    borrow_date: datetime = datetime.utcnow()

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
            raise Exception("This user is already registered.")

        self.members.append(member)

        print(f"Member {member.name} is registered.")
    
    def register_book(self, book: Book):
        self.books.append(book)
    
    def lend_book(self, member: Member, book: Book):

        active_late_lendings = filter(lambda transaction: transaction.member == member and transaction.last_give_back_date < datetime.utcnow(), self.lending_transactions)
        if active_late_lendings:
            raise Exception("You are late for some books. Please, give back them first.")
        
        late_lendings = filter(lambda transaction: transaction.member == member and transaction.last_give_back_date < transaction.give_back_date, self.lending_transactions)
        total_penalty = ceil(sum((transaction.give_back_date - transaction.last_give_back_date).days for transaction in late_lendings)) * self.daily_penalty_for_late_give_back
        
        payments = filter(lambda transaction: transaction.member == member, self.payment_transactions)
        total_payment = sum(payment.amount for payment in payments)

        if total_payment < total_penalty:
            required_payment = total_penalty - total_payment
            raise Exception(f"Please pay your penalty. Total: {required_payment:.6f}")

        active_lendings = filter(lambda transaction: transaction.member == member and transaction.is_active == True, self.lending_transactions)

        if len(active_lendings) >= self.default_lending_count:
            raise Exception("You have reached library book lending limit. Please, give back some of our books.")
        
        active_same_lendings = filter(lambda transaction: transaction.member == member and transaction.book == book and transaction.is_active == True, self.lending_transactions)
        if active_same_lendings:
            raise Exception(f"You have this book.")
        
        # Kullanici toplamda librarynin limitine dayanmissa


if __name__ == "__main__":
    print("serkan")