#--------------------------
if 9>7:
    if 6>3:
        print("HI")

#--------------------------
if 7>3:
    if 7>8:
        print("HI")
    else:
        print("BYE")
        
# Finding Largest Number from 3 numbers

num1=float(input("Enter The First Number : "))
num2=float(input("Enter The Second Number : "))
num3=float(input("Enter The Third Number : "))

if num1>num2:
    if num1>num3:
        print("The Largest Number is ",num1)
    else:
       print("The Largest Number is ",num3) #ei line na dileo hoto (may be)
        
if num2>num1:  #also can be used = else:
    if num2>num3:
        print("The Largest Number is ",num2)
    else:
        print("The Largest Number is ",num3)
           