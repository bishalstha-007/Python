class student:
    def __init__ (self, name, grade):
        self.name = name 
        self.grade = grade

    def display(self):
            print(f"Name : {self.name}")
            print(f"Grade : {self.grade}")

student1 = student("Bishal", "A")
student1.display()