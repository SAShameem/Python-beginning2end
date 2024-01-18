class Student:
    roll = ""
    gpa = ""

rahim = Student()
# Object Check:::   print(isinstance(rahim,Student))
rahim.roll = 232
rahim.gpa = 3.90
print(f"Roll: {rahim.roll}, GPA = {rahim.gpa}")

print("========-----========")

karim = Student()
karim.roll = 233
karim.gpa = 3.33
print(f"Roll: {karim.roll}, GPA = {karim.gpa}")

