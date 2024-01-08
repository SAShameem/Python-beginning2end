books = []
books.append("Concept Of Physics")
books.append("Learn C")
books.append("Python For Babies!")
books.append("ICT")

print(books)

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
if not books:
    print("No books left")