sonuc=all([False,False]) #hepsi aynıysa aynı olan değer döner
print(sonuc)
sonuc=any([True,False,True]) #herhangi biri true ise true
print(sonuc)

sayilar=[1,2,3,4,5,6,7,8,9]
sonuc=all([bool(sayi) for sayi in sayilar ])
print(sonuc)