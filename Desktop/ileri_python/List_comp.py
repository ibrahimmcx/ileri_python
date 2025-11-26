
sayilar=[]
for i in range(5):
    sayilar.append(i)
#list comprehension
liste=[i for i in range(5)]    
print(liste)

kurum="btk akademi"
for i in kurum :
    print(i.upper())

liste =[i.upper for i in kurum] 
print(liste)

#koşullu durumlar
liste=[10,20,30,40,50,60,70,80,90]
for item in liste :
    if item %2==0:
       print(item)
#çift sayıları yazdıran list comprehension

sonuc = [item for item in liste if item %2==0]
print(liste)

sonuc =[  i if i%2==0  else "tek sayı" for i in liste ]
print (sonuc)

urun_fiyatlari=[0,100,200,300,400,500]
vergiler=[fiyat *1.2 for fiyat in urun_fiyatlari if fiyat>0]
vergiler=[fiyat*1.2 if fiyat>0 else "vergi hesaplanmadı" for fiyat in urun_fiyatlari   ]
print(vergiler)


#1 ve 1000 arasında 12 e tam bölünen sayıları listeleyen list comprehension

sonuc =[i for i in range(1,101) if i%12==0]
print(sonuc)

#verilen text içerisindeki sayıları listeleyen list comprehension
liste =["hello 12 world","456"]
sonuc =[i for i in liste if i.isdigit()]
print(sonuc)

#sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi var yazdırın
sıcaklıklar=[10,20,30,0,-2,-15,25,30,40]
sonuc=[i if i>= 4 else "buzlanma tehlikesi"for i in sıcaklıklar  ]
print(sonuc)

#öğrenciler ve notlar listesindeki notu 50 den fazla olan kişileri ekrana dict verisine yazdırın
öğrenciler=["ali","veli","ayşe","fatma"]
notlar=[10,20,50,70]
sonuc =[(öğrenciler[i],notlar[i]) for i in range(len(öğrenciler)) ]
liste_dict={key:value for (key,value) in sonuc if value>50}
print(liste_dict)


#for döngüsü ile yazılan uygulamayı list comprehension ile yazınız
sonuc=[]
for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

sonuc= [(x,y) for i in range(3) for y in range(3) ]
print(sonuc)       