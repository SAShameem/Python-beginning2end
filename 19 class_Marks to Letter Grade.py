#marks to letter grade:

marks=float(input("Enter Your Marks: "))

if marks>=80 and marks <=100:
    print("A+")
elif marks>=70 and marks <=79:
    print("A")
    
#one more way:
marks=float(input("Enter Your Marks: "))

if 80<=marks<=100:
    print("A+")
elif 70<=marks<=79:
    print("A")