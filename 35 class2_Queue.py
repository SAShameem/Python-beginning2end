#first in, first out like a bank service


bank = ["x","y","a"] #example

from collections import deque

bank = deque(["SAS", "GURU", "Nasim"])
bank.popleft ()
# (bank service dichche)
print (bank)

bank.popleft ()
bank.popleft ()



if not bank:
    print("No person left")
    
    