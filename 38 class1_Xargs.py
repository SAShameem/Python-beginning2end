#xargs

def student (id,name):
    print(id,name)
student(101,"SAMIM")

#Or,
def student (*details):
    print(details[1])
student(101,"SAMIM", 3.87,) 

#######
def add(num1,num2):
    sum=num1+num2
    print(sum)
add(10,20)

####
def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
    
add(10,20)
add(10,20,30)
add(10,20,30,40)

