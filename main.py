from typing import runtime_checkable
from models import *

if __name__ == "__main__":
    richmond_library = Library(name="Richmond Library", default_lending_day=20, default_lending_count=3, daily_penalty_for_late_give_back=2)
    twickenham_library = Library(name="Twickenham Library", default_lending_day=15, default_lending_count=2, daily_penalty_for_late_give_back=1)

    book_avucunuzdaki_kelebek = Book(name="Avucunuzdaki Kelebek", isbn="68618505147")
    book_hortumlu_dunya = Book(name="Su hortumlu dunyada fil yalniz bir hayvandir", isbn="68618505148")
    book_nutuk = Book(name="Nutuk", isbn="68618505149")
    book_python = Book(name="Python", isbn="68618505150")
    member_serkan_uz = Person(name="Serkan Uz")
    member_utku_atak = Person(name="Utku Atak")

    lending1 = LendingTransaction(member_utku_atak,book_python,last_give_back_date=datetime.strptime("20221201","%Y%m%d"),give_back_date=datetime.strptime("20221231","%Y%m%d"))
    lending2 = LendingTransaction(member_serkan_uz,book_python,last_give_back_date=datetime.strptime("20221201","%Y%m%d"),give_back_date=datetime.strptime("20221231","%Y%m%d"))
    lending3 = LendingTransaction(member_serkan_uz,book_python,last_give_back_date=datetime.strptime("20221201","%Y%m%d"),give_back_date=datetime.strptime("20221231","%Y%m%d"))

    richmond_library.register_book(book_avucunuzdaki_kelebek)
    richmond_library.register_book(book_avucunuzdaki_kelebek)
    richmond_library.register_book(book_hortumlu_dunya)
    richmond_library.register_book(book_nutuk)
    richmond_library.register_book(book_python)

    richmond_library.register_member(member_serkan_uz)
    richmond_library.register_member(member_serkan_uz)
    richmond_library.register_member(member_utku_atak)
    richmond_library.register_lending(lending1)
    # richmond_library.register_lending(lending2)
    # richmond_library.register_lending(lending3)
    
    


    richmond_library.show_members()

    richmond_library.active_book_list()
    

    # richmond_library.lend_book(member_serkan_uz,book_avucunuzdaki_kelebek)
    # richmond_library.lend_book(member_serkan_uz,book_hortumlu_dunya)
    # richmond_library.lend_book(member_serkan_uz,book_hortumlu_dunya)
    richmond_library.lend_book(lending1)
    richmond_library.lend_book(lending2)
    richmond_library.lend_book(lending3)   

    

    richmond_library.find_member_penalty(lending1)
    richmond_library.find_member_penalty(lending2)

    #richmond_library.total_library_money()