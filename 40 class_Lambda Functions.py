# Named Function:
def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2,3))


# Lambda Function:
## General Structure : ##
# lambda parameter : expression #

(lambda a,b : a*a + 2*a*b + b*b)

print(calculate(2,3))

#Or,
a = (lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(a)

#Or,
print((lambda a,b : a*a + 2*a*b + b*b)(2,3))


### Cube:
a = (lambda x : x*x*x)(2)
print(a)