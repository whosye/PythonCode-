# creating a pokemon 

class Pokemon:
    def __init__(self, name, primary_type):
        self.name = name
        self.primary_type =  primary_type
    
    def __str__(self): # kdyz vyprintim boject na primo, tak dostanu obsah pod __str__ 
        return f'{self.name }  {self.primary_type}'
        


Bulbasaur = Pokemon('mrdka', 'grass')
 




if __name__ == '__main__': # podmnka se spusti pouze pokud se spusti skript na primo 
    pass
   # print(Bulbasaur.name)
   # print(Bulbasaur.primary_type)
