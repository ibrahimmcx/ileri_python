sayilar =[1,2,3,4,5,6,7,8,9]
kareler=[]
for i in sayilar:
    kareler.append(i**2)
print(kareler)

#map fonksiyonu
def kareal(x):
    return x**2
sonuc=map(kareal,sayilar)
print(list(sonuc))