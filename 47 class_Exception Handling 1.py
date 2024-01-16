## EXCEPTION = Runtime error/Incorrect Input/Incorrect Code :
# int na dile error dekhabe
num2 = int(input("Enter a number : "))
result = 20/num2
print(result)
print("Done")

## Another Example : (INDEX ERROR)
'''
text = "SAMIM"
print(text[6])
print("Done")
'''
# Index Error Handling:
try:
    text = "SAMIM"
    print(text[6])
    print("Done")
except IndexError:
    print("Index Error")

#### Exception Handling :
try:
    list = [20,0,30]
    result = list[0]/list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally: #Avoiding errors it will be printed
    print("Successful")

