class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


"""
book = Book('Bold', 'Diamantis', 330)
print(book.author, book.name, book.pages)
print(Book('Bold', 'Diamantis', 330).__dict__)
"""
