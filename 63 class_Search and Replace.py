## sub function:

# sub(pattern, replace, string)

import re
pattern = r"colour"
text1 = "My FAV colour is Orange. I love Red colour also."
text2 = re.sub(pattern, "color", text1)
print(text2)

#count=1 for only first word change.... 2 for first 2....
import re
pattern = r"colour"
text1 = "My FAV colour is Orange.I love Red colour also."
text2 = re.sub(pattern, "color", text1,count=1)
print(text2)