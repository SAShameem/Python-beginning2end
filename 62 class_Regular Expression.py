import re
pattern = r"colour"
if re.match(pattern,"colour is a colour, I love red co	lour"):
    print("Mached")
else:
    print("Not Matched")
################# 
import re
pattern = "colour"
if re.search(pattern,"Red is a colour, I love red colour"):
    print("Mached")
    
    
###################
import re
pattern = "colour"
if re.findall(pattern,"Red is a colour, I love red colour"):
    print("Mached")
                
print("===============----------==========")


import re
pattern = r"colour"
text1 = "My fav. colour is Red. Iovw blue also..."