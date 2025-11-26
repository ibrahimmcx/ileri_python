sayilar=[1,2,3,4,5,6,7,8,9]
sonuc=sum(sayilar)#sayıları toplar
sonuc=sum(sayilar,5)#sayıları toplar ve 5 ekler
products=[
    {"urun_adi":"samsung s20","fiyat":5000},
    {"urun_adi":"samsung s30","fiyat":6000},
    {"urun_adi":"samsung s10","fiyat":4000}]
toplamFiyat=sum([urun["fiyat"] for urun in products])
urunAdeti=len([urun for urun in products if urun["fiyat"]>0])
sonuc=toplamFiyat/urunAdeti


print(sonuc)