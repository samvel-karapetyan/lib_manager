# main.py <- head of code (python main.py)
# src--
#     |--manager.py <- class LibraryManager
#     |--book.py <- class Book
# data--
#     |--library_data.json
#     |--logs.txt
from src.manager import LibraryManager
from src.book import Book

# git - version control

# git status - ընդհանուր վիճակը
# git add - ավելացնել ֆայլեր
# git commit - ստեղծել փոփոխություն
# git push - ուղարկել github

# git pull - commit-ները բերել մեր մոտ


def run_library_manager():
    manager = LibraryManager()
    
    while True:
        command = input("Command (add/remove/search/exit): ")
        manager.process(command)

        if command == "exit":
            break

if __name__ == "__main__":
    run_library_manager()

# python main.py