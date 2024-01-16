
num= [1,2,3,4,5]

# [Expression for item in list]

result = [x*x for x in num]

#The line is Alternative Of ==>  result = list(map(square,num))

print(result)

## Filter Example:

num= [1,2,3,4,5]

# [Expression for item in list if Condition]
result = [x for x in num if x%2==0]

#The Line is T Alternative Of ==>  result = list(filter(lambda x : x%2 == 0,num))
print(result)