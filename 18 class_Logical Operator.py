# Finding Largest Number from 3 numbers

num1=float(input("Enter The First Number : "))
num2=float(input("Enter The Second Number : "))
num3=float(input("Enter The Third Number : "))

if num1>num2 and num1>num3:
    print("The Largest Number is ",num1)
    
elif num2>num1 and num2>num3:
    print("The Largest Number is ",num2)
    
else:
    print("The Largest Number is ",num3)
    
#Vowel & consonant finding
    
ch= str(input("Enter The Character : "))

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("It's Vowel")
else:
    print("It's Consonant")