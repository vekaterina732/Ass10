# library.py

class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        """Initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        """Return information about the book."""
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: ${self.price:.2f}, Stoplist: {self.stoplist}"

    @classmethod
    def find_most_expensive(cls, books):
        """Return the most expensive book from a list of books."""
        if not books:
            return None
        most_expensive = max(books, key=lambda book: book.price)
        return most_expensive

    def set_stoplist(self, boolean):
        """Set the stoplist attribute."""
        self.stoplist = boolean

    def censor(self, author_name, boolean):
        """Set stoplist based on author name."""
        if self.author == author_name:
            self.stoplist = boolean
