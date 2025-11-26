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

class Coupon:
    def __init__(self,code,discount):
        self.code=code
        self.discount=discount
c1=Coupon("indirim10",0.8)
c2=Coupon("indirim20",0.6)
c3=Coupon("indirim30",0.4)        
class ShoppingCard:
    coupon_list=[c1,c2,c3]
    def __init__(self,liste):
        self.liste=liste
    def add_item(self,item) :
        self.liste.append(item)   
    def display_items (self) :
        for i in self.liste:
            print(f"{i.name} {i.price} {i.quantity}")
    def calculate_totals(self):
        return sum([item.calculate_total_price for item in self.liste])          
    def remove_item(self,cart_item):
        self.liste=[item for item in self.liste if item!=cart_item]
    def clear(self):
        self.liste.clear()
    @classmethod
    def get_coupons(cls)    :
        return [coupon.code for coupon in cls.coupon_list]
    @classmethod
    def get_coupon(cls,code):
        return next(filter(lambda c:c.code==code,ShoppingCard.coupon_list))

    def apply_coupon(self,code):
        if code not in ShoppingCard.get_coupons():
            raise ValueError(f"{code} geçersiz kupon kodu")
        coupon=ShoppingCard.get_coupon(code)
        for index in range(len(self.liste)):
            self.liste[index].price=self.liste[index].price*coupon.discount




item1=CartItem("iphone 14",1000,2)
item2=CartItem( "iphone 15",10000,1)
item3=CartItem("samsung s23",2000,3)
print(CartItem.display_item_count())
CartItem.create_item("xiaomi,5000,3")
print(CartItem.display_item_count())

shopping_cart=ShoppingCard([item1,item2])
shopping_cart.add_item(item3)
shopping_cart.display_items()
shopping_cart.apply_coupon("indirim20")
shopping_cart.display_items()

