## Writing in File:
# Append (new line add) = a
# Write (all delete & write) = w
# .txt new name = new file create

file = open("ReadingAFile.txt","a")
#file = open("ReadingAFile.txt","w")
#file = open("ReadingAFileNew.txt","w")

file.write("\nTASMIM = GADHA")

file.close()
