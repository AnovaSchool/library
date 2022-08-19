from models import *

if __name__ == "__main__":
    richmond_library = Library(name="Richmond Library", default_lending_day=20, default_lending_count=3, daily_penalty_for_late_give_back=2)
    twickenham_library = Library(name="Twickenham Library", default_lending_day=15, default_lending_count=2, daily_penalty_for_late_give_back=1)

    book_avucunuzdaki_kelebek = Book(name="Avucunuzdaki Kelebek", isbn="68618505147")
    book_hortumlu_dunya = Book(name="Su hortumlu dunyada fil yalniz bir hayvandir", isbn="68618505148")
    book_nutuk = Book(name="Nutuk", isbn="68618505149")
    book_python = Book(name="Python", isbn="68618505150")

    member_serkan_uz = Member(name="Serkan Uz")
    member_utku_atak = Member(name="Utku Atak")

    richmond_library.register_book(book_avucunuzdaki_kelebek)
    richmond_library.register_book(book_hortumlu_dunya)
    richmond_library.register_book(book_nutuk)
    richmond_library.register_book(book_python)

    richmond_library.register_member(member_serkan_uz)
    richmond_library.register_member(member_serkan_uz)
    richmond_library.register_member(member_utku_atak)

    richmond_library.show_members()

    richmond_library.giveback_book_list()

    richmond_library.lend_book(member_serkan_uz,book_avucunuzdaki_kelebek)
    ## bu daha ilk lend book ve you are late for some books uyarısı alıyoruz.
    richmond_library.lend_book(member_serkan_uz,book_hortumlu_dunya)
    richmond_library.lend_book(member_serkan_uz,book_hortumlu_dunya)
    richmond_library.lend_book(member_serkan_uz,book_nutuk)
    richmond_library.lend_book(member_serkan_uz,book_python)   
    