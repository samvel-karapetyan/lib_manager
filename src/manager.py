from src.book import Book
from constants import DATA_PATH
import json
import os

# github |
# todo |
# streamlit <-
# TODO: log all operations

class LibraryManager:
    def __init__(self):
        # 1. if DATA_PATH does not exist
        # 2. convert dict -> Book

        if os.path.exists(DATA_PATH): # True/False
            with open(DATA_PATH) as f:
                data = json.load(f)

            # map(lambda book_dict : Book.from_dict(book_dict), data)
            self._books = list(map(Book.from_dict, data))
        else:
            self._books = [] # list[Book, Book, Book, Book]

    def _get_books(self):
        return self._books

    def _add_book(self, book):
        self._books.append(book)

    def add_with_input(self):
        print("Adding book...")
        title = input("Input the title: ")
        while True:
            try:
                publication_year = int(input("Enter the publication year: "))
            except ValueError:
                print("...Wrong year...")
            else:
                break

        author = input("Enter the author's name: ")
        genre = input("Input the genre: ")

        self.add(title=title, publication_year=publication_year, author=author, genre=genre)

    def add(self, title, publication_year, author, genre):
        book = Book(
            title=title,
            publication_year=publication_year,
            author=author,
            genre=genre
        )

        self._add_book(book)
        print("Book added...")

    def remove_with_input(self):
        print("Removing book...")
        title = input("Input the title: ")
        author = input("Enter author's name: ")

        self.remove(title=title, author=author)

    def remove(self, title, author):
        # for i, book in enumerate(self.books):
        #     if book.check_book(title=title, author=author):
        #         del self.books[i] <- vaxenalu ban

        self.books = list(
            filter(
                lambda book : not book.check(title=title, author=author), 
                self.books
                )
            )
        
        print("Book removed...")
    
    def search_with_input(self):
        print("Searching book...")
        keyword = input("Input the keyword: ")

        self.search(keyword=keyword)

    def search(self, keyword):
        filtered_books = list(filter(lambda book : book.contains(keyword), self.books))
        print(filtered_books)

        return filtered_books

    def exit(self):
        print(self.books)
        with open(DATA_PATH, "w") as f:
            # self.books -> [book1, book2, book3, book4]
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def process(self, command):
        match command:
            case "add":
                self.add_with_input()
            case "remove":
                self.remove_with_input()
            case "search":
                self.search_with_input()
            case "exit":
                self.exit()

# manager._books()
# manager._get_books() # protected variable/method # -> [Book, Book, Book] ?
# manager.add, manager.add_with_input