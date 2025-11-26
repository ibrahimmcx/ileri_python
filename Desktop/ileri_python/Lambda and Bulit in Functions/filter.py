sayilar=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
def negatifsayi(x):
    if x<0:
        return True
    else :
        return False

sonuc = list(filter(lambda x:x<0,sayilar))
print(sonuc)

sonuc =list(filter(lambda x:x%2==0,sayilar))
print(sonuc)

isimler=["ali","veli","ayşe","fatma","ahmet","mehmet"]
sonuc=list(filter(lambda x:x[0]=="a",isimler))
print(sonuc)

kullanıcılar=[
    {"ad":"ali","soyad":"yılmaz","post":["iyi geceler"]}, 
    {"ad":"veli","soyad":"demir","post":["merhaba","nasılsın"]}, 
    {"ad":"ayşe","soyad":"çelik","post":["merhaba"]},
    {"ad":"fatma","soyad":"yıldız","post":["günaydın"]},
    {"ad":"ahmet","soyad":"kaya","post":["merhaba","nasılsın"]},
    {"ad":"mehmet","soyad":"şahin","post":["merhaba","nasılsın"]},]
sonuc =list(map(lambda x:len(x ["post"])>1,kullanıcılar))
sonuc = list(map(lambda u:u["ad"],filter(lambda kullanıcı:len(kullanıcı["post"])>1,kullanıcılar)))
print(sonuc)