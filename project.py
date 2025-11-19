# Define Classes First

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}")
    
    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' joined {self.name}")
    
    def show_available_books(self):
        print(f"\nAvailable books in {self.name}:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author}")


# -------------------------------
# Usage Code (Now it will work!)
# -------------------------------

# Create Library
library = Library("City Library")

# Add Books
book1 = Book("Python Basics", "Guido van Rossum")
book2 = Book("Data Science Handbook", "Jake VanderPlas")
book3 = Book("Clean Code", "Robert C. Martin")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add Members
member1 = Member("Madhu", 101)
member2 = Member("Anita", 102)

library.add_member(member1)
library.add_member(member2)

# Borrow and Return
library.show_available_books()
member1.borrow_book(book1)
member2.borrow_book(book1)  # Already borrowed
member2.borrow_book(book2)

library.show_available_books()
member1.return_book(book1)
library.show_available_books()
