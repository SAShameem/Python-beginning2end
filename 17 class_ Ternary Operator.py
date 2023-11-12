#Finding Largest Number:
num1=float(input("Enter The First Number : "))
num2=float(input("Enter The Second Number : "))

'''
if num1>num2:
    print(num1)
else:
    print(num2)
'''
#The easiest way:
#Using Ternary Operator:

max=num1 if num1>num2 else num2
print("The Largest Number is ",max)


