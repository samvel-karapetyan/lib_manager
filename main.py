# main.py <- head of code (python main.py)
# src--
#     |--manager.py <- class LibraryManager
#     |--book.py <- class Book
# data--
#     |--library_data.json
#     |--logs.txt
from src.manager import LibraryManager
from src.book import Book


def run_library_manager():
    manager = LibraryManager()
    
    while True:
        command = input()
        manager.process(command)

        # TODO: if command exit, it should end the program

if __name__ == "__main__":
    run_library_manager()

# python main.py