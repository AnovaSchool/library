LIBRARY 

Class definitions of Library project

Person
name - string

Member (Person sınıfından türeyecek)
Employee (Person sınıfından türeyecek)  

Book
name - string
isbn - string


LendingTransaction
member - Member object
book - Book object
last_give_back_date_time - datetime
id - str
give_back_date_- datetime
borrow_date - datetime
is_active - bool - Eğer kitap geri verilmişse False değilse True.

PaymentTransactions
Member - member 
Amount - decimal
created_at - datetime	

Library 
name - str
lending_day - int 
lending_count - int 
daily_penalty_for_late_give_back - Decimal
members - List of member
lending_transactions - list of Lending Transaction
payment_transactions: list of Payment Transaction
books: list of Book
created_at - datetime


Functions
Library definition with default lending day.
Add books to library. Books will add to the books that we created in Library class.
Register member to the library.Members will add to the members that we created in Library class. Same person can't register again.
Lend book. Lending transactions will add to the lending transactions that we created in Library class. Member can't get the same book twice. If a user has penalty user can't lend new book. User can lend maximum 3 books.

Return the book to the library. 
List the members of library.
Calculate the total penalty of an user. If an user holds book over 15 days user pays penalty for each day of library's penalty amount of a day. 
User penalty payment 
How much money Library's got ? 
