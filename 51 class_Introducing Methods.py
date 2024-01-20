class Student:
    roll = ""
    gpa = ""
    
    def display(self):
        print(f"Roll: {self.roll}, GPA = {self.gpa}")

karim = Student()
karim.roll = 233
karim.gpa = 3.33
karim.display()

print("========-----========")

rahim = Student()
rahim.roll = 232
rahim.gpa = 3.90
rahim.display()

print("========-----========")
print("========-----========")

### Or,
class Student:
    roll = ""
    gpa = ""
    
    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    
    def display(self):
        print(f"Roll: {self.roll}, GPA = {self.gpa}")

karim = Student()
karim.set_value(102,4.5)
karim.display()

print("========-----========")

rahim = Student()
rahim.set_value(234,5.00)
rahim.display()
