class CartItem:
    #constructor => yapıcı method
    discount_rate=0.8
    item_count=0
    
    def __init__(self ,name,price,quantity):
        #instance attribues => örnek nitelikler
        self.name=name
        self.price=price    
        self.quantity=quantity
        CartItem.item_count+=1

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price=self.price*CartItem.discount_rate       
#instance => nesne örnek
item1=CartItem("iphone 14",1000,2)
item2=CartItem( "iphone 15",10000,1)
item3=CartItem("samsung s23",2000,3)


print(CartItem.discount_rate)
item1.apply_discount()
item2.apply_discount()
item3.apply_discount()
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())
print(CartItem.item_count)
print(item1.__dict__)
print(item2.__dict__)   
print(item3.__dict__)