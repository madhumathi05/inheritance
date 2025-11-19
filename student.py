class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
    
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Course: {self.course}")

# Example usage
s1 = Student("Madhu", 101, "Data Science")
s2 = Student("Anita", 102, "Web Development")

s1.display_info()
s2.display_info()
