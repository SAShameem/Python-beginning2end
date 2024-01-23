#Inheritance:: (Existing code ke babohar kora)
# Parent class, Super class, Base class
#Child class, Sub class, Derived Class

## Normal Code:
class Phone:
    def call(self):
        print("You can Call")
    
    def message(self):
        print("You can Message")
    
class Samsung:
    def call(self):
        print("You can Call")
    
    def message(self):
        print("You can Message")
    
    def photo(self):
        print("You can take Photo")
p = Phone()
p.message()
p.call()

s = Samsung()
s.call()
s.message()
s.photo()

print("=====--BREAK--=====")

## Code Using Inheritance:
class Phone:
    def call(self):
        print("You can Call")
    
    def message(self):
        print("You can Message")
    
class Samsung(Phone): #Phone er ekta catagory Samsung(Phone CLASS er boisisto Samsung e thakbe.)
    #Class: Phone; Sub-Class: Samsung
    def photo(self):
        print("You can take Photo")
p = Phone()
p.message()
p.call()

s = Samsung()
s.call()
s.message()
s.photo()


### Sub-Class Check:
print(issubclass(Samsung,Phone))
#       Right:  (Sub-Class,Class)
print(issubclass(Phone,Samsung))

