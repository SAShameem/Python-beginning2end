
#1*2*3*........*n
n=int(input("Enter the last number : "))

sum=1
for x in range (1,n+1,1):
    sum=sum*x
print(sum)

# n!
n=int(input("Enter the last number : "))

sum=1
for x in range (1,n+1,1):
    sum=sum*x
print(sum)



#1^2*2^2*3^2*..........*n^2
#1*1x2*2x3*3x....xn*n (simple format)
n=int(input("Enter the last number : "))

sum=1
for x in range (1,n+1,1):
    sum=sum*x*x
print(sum)


#2^2*4^2*6^2*..........*n^2
#2*2x4*4x6*6x....xn*n (simple format)
n=int(input("Enter the last number : "))

sum=1
for x in range (2,n+1,2):
    sum=sum*x*x
print(sum)
