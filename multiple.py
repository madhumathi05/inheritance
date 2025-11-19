class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
    
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Course: {self.course}")


# Now create objects
student1 = Student("Ravi", 103, "AI")
student2 = Student("Priya", 104, "Cybersecurity")
student3 = Student("Arjun", 105, "Cloud Computing")

student1.display_info()
student2.display_info()
student3.display_info()
