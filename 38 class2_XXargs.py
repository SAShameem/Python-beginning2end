#xxargs

def student (id,name):
    print(id,name)
    
student(101,"SAS")



### xxargs = 2 ta **

def student (**details):
    print(details)
    
    print(details["ID"])
    print(details["Name"])
    
    
student(ID=101,Name="SAS")