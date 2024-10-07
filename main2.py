# main2.py

from library import Book

# Create a list of different books
books = [
    Book("Book One", "Author A", 2020, 29.99),
    Book("Book Two", "Author B", 2018, 19.99),
    Book("Book Three", "Author A", 2021, 39.99, True),
    Book("Book Four", "Author C", 2019, 24.99),
    Book("Book Five", "Author D", 2023, 49.99),
]

# Print information for each book
print("Books Information:")
for book in books:
    print(book.get_info())

# Find and display the most expensive book
most_expensive_book = Book.find_most_expensive(books)
print("\nMost Expensive Book:")
if most_expensive_book:
    print(most_expensive_book.get_info())

# Set the stoplist for a specific book
books[0].set_stoplist(True)
print("\nUpdated Stoplist for Book One:")
print(books[0].get_info())

# Censor a book by author name
books[1].censor("Author B", True)
print("\nUpdated Stoplist for Book Two:")
print(books[1].get_info())