class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print("title: {self.title}", "\n", "author:{self.author}", "\n", ' pages : {self.pages}', "\n")


class Library:
    def __init__(self):
        self.books = []

    def add_Book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display()


book1 = Book("Python", "<sara>", 100)
book2 = Book("Python", "<ben>", 200)

my_library = Library()
my_library.add_Book(book1)
my_library.add_Book(book2)

my_library.show_books()
