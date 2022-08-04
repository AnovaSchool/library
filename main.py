from models import *


if __name__ == "__main__":
    richmond_library = Library(name="Richmond Library", default_lending_day=20, default_lending_count=3)
    twickenham_library = Library(name="Twickenham Library", default_lending_day=15, default_lending_count=2)

    book_avucunuzdaki_kelebek = Book(name="Avucunuzdaki Kelebek", isbn="68618505147")
    book_hortumlu_dunya = Book(name="Su hortumlu dunyada fil yalniz bir hayvandir", isbn="68618505148")

    member_serkan_uz = Member(name="Serkan Uz")

    richmond_library.register_book(book_avucunuzdaki_kelebek)
    richmond_library.register_book(book_hortumlu_dunya)

    richmond_library.register_member(member_serkan_uz)
    richmond_library.register_member(member_serkan_uz)
    





