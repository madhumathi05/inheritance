# Base class
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# Derived class
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
    
    def study(self):
        print(f"{self.name} is studying {self.course}")

# Example usage
t1 = Teacher("Dr. Rao", "Data Science")
s1 = Student("Madhu", "Python Programming")

t1.greet()
t1.teach()
s1.greet()
s1.study()
