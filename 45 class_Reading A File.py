## Reading A File:
# Reading = r
# Writing = w
# Reading + Writing = r+

file = open("ReadingAFile.txt","r")

print(file.readable())

text = file.read()
print(text)
size=len(text)
print(size) # size in character
file.close()


print("-----------------------")
## File in List:
file = open("ReadingAFile.txt","r")

text = file.readlines()
#text = file.readlines()[0]
#text = file.readlines()[1]

print(text)
file.close()

## Using For Loop:

file = open("ReadingAFile.txt","r")
for line in file :
    print(line)
file.close



