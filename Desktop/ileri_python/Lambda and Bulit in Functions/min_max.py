sayilar=[1,2,3,4,5,6,7,8,9]
harfler=["a","b","c","d","e","f"]
isimler=["ali","veli","ayşe","fatma"]

sonuc=min(sayilar) #1
sonuc=max(sayilar)#2
sonuc=min(harfler)#"a"
sonuc=max(harfler) #"f"
sonuc=min(isimler) #"ali"
sonuc=max(isimler) #"veli"  

sonuc=max([len(isim) for isim in isimler])

sonuc=min([len(isim) for isim in isimler]) #5
sonuc=max(isimler ,key=lambda isim:len(isim)) #fatma
sonuc=min(isimler ,key=lambda isim:len(isim)) #ali
urunler=[
    {"urun_adi":"samsung s20","fiyat":5000},    
    {"urun_adi":"samsung s30","fiyat":6000},
    {"urun_adi":"samsung s10","fiyat":4000}]
sonuc=min(urunler,key=lambda urun :urun["fiyat"])
sonuc=max(urunler,key=lambda urun:urun["fiyat"])


print(sonuc)
