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


Fonksiyonlar
Library definition with default lending day.
Kütüphaneye kitap ekleme. Kütüphane içerisindeki books’a eklenecek. 
Kütüphaneye üye ekleme. Kütüphane içerisindeki member’a eklenecek. Aynı kişi tekrar üye olarak eklenemez.
Kitap ödünç alma. Kütüphane içerisindeki transactions’a eklenecek. Aynı kitap aynı kullanıcı tarafından aynı anda 2 defa ödünç alınamayacak. Kullanıcının hali hazırda borcu varsa o zaman yeni kitap alamaz. Bir üye aynı anda en fazla 3 kitap alabilir.
Kitap geri verme. 
Şu an kütüphaneden ödünç alınan ve geri getirilmeyen kitapların listesi.
Şu an kütüphaneden ödünç alınan ve süresinde geri getirilmemiş kitapların listesi. Normal geri verme süresi 15 gündür.
Kütüphane üyelerini listeleme.
Bir kullanıcının toplam cezasını hesaplama. Bir kitabı 15 günden fazla elinde tutarsa her gün için 3 TL ceza öder.
Kullanıcı ceza ödeme. 
Library’de şu an ne kadar para var?

