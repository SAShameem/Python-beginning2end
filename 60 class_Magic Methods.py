### Magiic Methods:

#Magic Methods for Comparison:
'''
__eq__(self, other)
__ne__(self, other)
__lt__(self, other)
__gt__(self, other)
__le__(self, other)
__ge__(self, other)
------------------
== Python also provides Magic Methods for Comparison:
__eq__() for ==
__ne__() for!=
__lt__() for <
__gt__() for >
__le__() for <=
__ge__() for >=

'''
#Magic Methods for Arithmetic Calculation:

'''
__add__(self, other)
__sub__(self, other)
__mul__(self, other)
__div__(self, other)

'''

## Practical:
class bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __eql__(self,other):
        return self.name == other.name and self.color == other.color
        
    def __str__(self):
        return(f"Name = {self.name}, Color = {self.color}")
    
    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = bike("Yamaha R15", "Blue")
bike2 = bike("Yamaha FZ", "Red")
bike3 = bike("Yamaha R15", "Blue")

print(bike1)
print(str(bike2))
print(bike1==bike3) 
