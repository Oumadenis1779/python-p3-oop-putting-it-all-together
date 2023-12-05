#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self._size=size
        self.condition = 'New'

    def get_size(self):
        return self._size
        
    def set_size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")
    
    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
        return("The shoe has been repaired.")

    size=property(get_size,set_size,)
    pass
Prada=Shoe("Prada",9)
print(Prada.size)
print(Prada.brand)
print(Prada.cobble())