class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True
    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False
    def return_book(self):
        if not self.__available:
            self.__available = True
            return True
        return False
    def status(self):
        return "Available" if self.__available else "Borrowed"
class Library:
    books = []
    @classmethod
    def add_book(cls, title, author):
        cls.books.append(Book(title, author))
    @classmethod
    def remove_book(cls, title):
        for book in cls.books:
            if book.title.lower() == title.lower():
                cls.books.remove(book)
                return True
        return False
    @classmethod
    def search(cls, title):
        for book in cls.books:
            if book.title.lower() == title.lower():
                return book
        return None
    @classmethod
    def list_books(cls):
        if not cls.books:
            print("No books in library.")
            return
        for book in cls.books:
            print(f"{book.title} by {book.author} - {book.status()}")
class User:
    def __init__(self, name):
        self.name = name
    def view_books(self):
        Library.list_books()
class Student(User):
    def borrow_book(self):
        title = input("Enter book title to borrow: ")
        book = Library.search(title)
        if book and book.borrow():
            print("Book borrowed successfully.")
        else:
            print("Book not available.")
    def return_book(self):
        title = input("Enter book title to return: ")
        book = Library.search(title)
        if book and book.return_book():
            print("Book returned successfully.")
        else:
            print("Invalid return request.")
    def search_book(self):
        title = input("Enter book title to search: ")
        book = Library.search(title)
        if book:
            print(f"{book.title} by {book.author}- {book.status()}")
        else:
            print("Book not found.")
class Librarian(User):
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        Library.add_book(title, author)
        print("Book added successfully.")
    def remove_book(self):
        title = input("Enter book title to remove: ")
        if Library.remove_book(title):
            print("Book removed successfully.")
        else:
            print("Book not found.")
#                    PRELOAD BOOKS
Library.add_book("Lord of Rings", "J.R.R. Tolkien")
Library.add_book("Spiderman", "Marvel")
Library.add_book("Maths", "NCERT")
Library.add_book("Science", "NCERT")
Library.add_book("Hindi", "NCERT")
Library.add_book("English", "NCERT")
#                    MAIN PORGRAM
def main():
    print("Welcome to Library Management System")
    role = input("Enter role (student / librarian): ").lower()
    name = input("Enter your name: ")
    if role == "student":
        user = Student(name)
        while True:
            print("\n   Student Menu   ")
            print("1. View Books")
            print("2. Search Book")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                user.view_books()
            elif choice == "2":
                user.search_book()
            elif choice == "3":
                user.borrow_book()
            elif choice == "4":
                user.return_book()
            elif choice == "5":
                print("THANK YOU!")
                break
            else:
                print("Invalid choice.")
    elif role == "librarian":
        user = Librarian(name)
        while True:
            print("\n   Librarian Menu    ")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. View Books")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                user.add_book()
            elif choice == "2":
                user.remove_book()
            elif choice == "3":
                user.view_books()
            elif choice == "4":
                print("THANK YOU!")
                break
            else:
                print("Invalid choice.")
    else:
        print("Invalid role selected.")
main()
