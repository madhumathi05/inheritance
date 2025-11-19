class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is not available")
    
    def return_book(self):
        self.available = True
        print(f"You returned '{self.title}'")

# Example usage
book1 = Book("Python Basics", "Guido van Rossum")
book1.borrow()
book1.borrow()
book1.return_book()
