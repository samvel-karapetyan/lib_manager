from src.book import Book
from constants import DATA_PATH
import json

# TODO: log all operations

class LibraryManager:
    def __init__(self):
        # TODO: Load the data from DATA_PATH
        self.books = []

    def add(self):
        print("Adding book...")
        title = input("Input the title: ")
        while True:
            try:
                publication_year = int(input("Enter the publication year: "))
            except ValueError:
                print("...Wrong year...")
            else:
                break

        author = input("Enter author's name: ")
        genre = input("Input the genre: ")

        book = Book(
            title=title,
            publication_year=publication_year,
            author=author,
            genre=genre
        )

        self.books.append(book)

    def remove(self):
        print("Removing book...")
        title = input("Input the title: ")
        author = input("Enter author's name: ")

        # for i, book in enumerate(self.books):
        #     if book.check_book(title=title, author=author):
        #         del self.books[i] <- vaxenalu ban

        self.books = list(
            filter(
                lambda book : not book.check(title=title, author=author), 
                self.books
                )
            )
    
    def search(self):
        print("Searching book...")
        keyword = input("Input the keyword: ")

        # TODO: Search with keyword

    def exit(self):
        with open(DATA_PATH, "w") as f:
            # self.books -> [book1, book2, book3, book4]
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def process(self, command):
        match command:
            case "add":
                self.add()
            case "remove":
                self.remove()
            case "search":
                self.search()
            case "exit":
                self.exit()