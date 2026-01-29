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

    def check(self, title, author):
        # if self.title == title and self.author == author:
        #     return True
        # else:
        #     return False
        
        return self.title == title and self.author == author