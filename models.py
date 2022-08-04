from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal
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

        pass

        # Kullanicinin borcu var mi? 
        # Kullanici o kitabi zaten odunc almissa ve geri vermemisse
        # Kullanici toplamda librarynin limitine dayanmissa


if __name__ == "__main__":
    print("serkan")