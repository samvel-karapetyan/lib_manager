class Book:
    def __init__(
            self,
            title,
            publication_year,
            author,
            genre
            ):
        self.title = title # object-variable
        self.publication_year = publication_year
        self.author = author
        self.genre = genre

    def to_dict(self):
        return dict(
            title=self.title,
            publication_year=self.publication_year,
            author=self.author,
            genre=self.genre
        )
    
    # staticmethod - իմաստային կապ ունեն class-ի հետ    > ոչ մի բան չի փոխանցվում
    # classmethod - կապ ունեն միայն class-ի հետ         > cls (Book)
    # method - կապ ունեն և class-ի, և օբյեկտի հետ       > self (Book օբյեկտ)

    @classmethod
    def from_dict(cls, book_dict: dict) -> Book:
        # cls(*list(book_dict.values()))

        # **{'title': '1984', 'publication_year': 1949, 'author': 'George Orwell', 'genre': 'Dystopian'}
        # title='1984', publication_year=1949, author='George Orwell', genre='Dystopian'

        return cls(**book_dict) # dictionary unpacking

    def check(self, title, author):
        # if self.title == title and self.author == author:
        #     return True
        # else:
        #     return False
        
        return self.title == title and self.author == author
    
    def contains(self, keyword: str) -> bool:
        return keyword in self.title \
            or keyword in str(self.publication_year) \
            or keyword in self.author \
            or keyword in self.genre
    
    # ???magic method??? # __str__, __repr__
    def __repr__(self): # representation # return "<path_to_class> object by <identifier>"
        return f"'{self.title}' by {self.author}"