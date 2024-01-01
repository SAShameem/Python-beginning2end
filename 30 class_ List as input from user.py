# Sum of numbers:

n = input ("Enter the numbers you want to do sum : ")
# 10 20 30 40 
list = n.split() #10, 20, 30, 40 
sum=0

for num in list:
    sum = sum + int (num)
    
print (sum)


# Letter, Digits, Words finder:

num0fWords=0
numofLetters=0
numofDigits=0

text= input("Enter a text of numbers: ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofLetters  = numofLetters + 1
        
    elif x >= '0' and x <= '9':
        numofDigits  = numofDigits + 1
        
    
    elif x == ' ':
        num0fWords  = num0fWords + 1
        
print("Numbers of Letters: ", numofLetters)
print("Numbers of Digits: ", numofDigits)
print("Numbers of Words: ", num0fWords+1)

        