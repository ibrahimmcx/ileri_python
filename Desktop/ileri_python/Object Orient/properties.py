class product :
    def __init__(self,name,price):
        self.name=name
        if price >=0:
            self._price=price
        else:
            raise ValueError("ürün fiyatı negatif olamaz")  
    @property    
    def price(self):
        return self._price    
    def price(self,value):
        if value >=0:
            self.value=value      
        else:
           raise ValueError("ürün fiyafı negatif olamaz")
    # def set_price(self,value):
    #     if value >=0:
    #         self.value=value      
    #     else:
    #         raise ValueError("ürün fiyafı negatif olamaz")
        
    # def get_price(self):
    #     return self._price  
     
p=product("Iphone 16",80000) 
print(p.price)
p.price=-90000
print(p.price)
# p.price=-75000 #değer atanır
# print(p.name,p.price)      
