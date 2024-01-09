#using return and function

## Returning Value From Function

def add(a,b):
    sum= a+b
    return sum
result = add(20,30)
print("Result= ",result)


#Large num. between 2 num:
def large (a,b):
    if a>b:
        return a
    else:
        return b
result = large (20,30)
print(result)

#Or,
print(large(100,30))


# evabeo kora jay.....
def large (a,b):
    if a>b:
        return a
    else:
        return b
max=large
print(max(99,1))
