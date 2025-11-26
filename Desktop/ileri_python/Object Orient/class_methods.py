class CartItem:
    #constructor => yapıcı method
    discount_rate=0.8
    item_count=0
    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count}tane ürün oluşturuldu"
    @classmethod
    def create_item(cls,data_str):
        name,price,quantity=data_str.split(",")
        return cls(name,price,quantity)
    
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
print(CartItem.display_item_count())
CartItem.create_item("xiaomi,5000,3")
print(CartItem.display_item_count())


