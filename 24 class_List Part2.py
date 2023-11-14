#using functions

subjects = ["C", "C++", "Java", "Python", "BD", "IN"]

print(len(subjects)) #len=length

# add to list at last
subjects.append("HTML")
print(subjects)

#to insert
subjects.insert(2,"MATLAB")
print(subjects)

#to remove
subjects.remove("IN")
print(subjects)

#sajano (choto theke boro)
subjects.sort()
print(subjects)

subjects = [20,30,25,5,8,2]
subjects.sort()
print(subjects)

#sajano (boro theke choto)
subjects.reverse()
print(subjects)

# last ta tule nite
subjects.pop()
print(subjects)

#sob item clear korte
subjects.clear()
print(subjects)

# list copy
subjects = [20,5,30,5,25,5,8,2]
subjects2=subjects.copy()
print(subjects2)

# item's position
pos=subjects.index(5)
print(pos)

#count
pos=subjects.count(5)
print(pos)


