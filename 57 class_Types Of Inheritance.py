'''Types of Inheritance'''
# 1. Heirarchical Inheritance
# 2. Multi-level Inheritance
# 3. Multiple Inheritance

### Multi-level Inheritance :
class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    #Display1
    def display2(self):
        print("I am inside B class")

class C(B):
     #Display1
     #Display2
    def display3(self):
        super().display1()
        super().display2() ### Display 1, 2 call
        print("I am inside C class")

ob1 = C()
ob1.display1()
ob1.display2()
ob1.display3()

print("=====--BREAK--=====")

### Multiple Inheritance :
class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")
'''
class C(A,B): #Here Priority is: C > A > B
    # A -> Display ()
    # B -> Display ()
    def display(self):
        print("I am inside C class")
'''   

class C(A,B): #Here Priority is: A > B
    # A -> Display ()
    # B -> Display ()
    pass
    

ob1 = C()
ob1.display()
