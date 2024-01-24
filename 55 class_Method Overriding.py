class Phone:
    def __init__(self):
        print(("I am in Phone class"))
        
class Samsung (Phone):
    #init
     def __init__(self):
         super().__init__()  """Super class ke call korte"""
         print(("I am in Samsung class"))
        

    
s = Samsung()