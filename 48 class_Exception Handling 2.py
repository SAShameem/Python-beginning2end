try:
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))
    result = num1/num2
    print(result)
        
# Errors in online
except (ValueError, ZeroDivisionError):
    print("You Have Entered Incorrect Input")
    
'''
except ValueError:
    print("You have to insert only integer.")
except ZeroDivisionError:
    print("You can not divide a number by 0")
finally:
    print("Thanks!!!")
'''

## Voter Check:

def voter (age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return ("You are allowed to Vote")
try:
    print(voter(18))
    print(voter(17))
except ValueError as error:
    print(error)