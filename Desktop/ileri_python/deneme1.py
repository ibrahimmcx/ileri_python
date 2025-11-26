num=[22,24,26,32,36]
yeni_sayilar=[ i*2 for i in num]
print(yeni_sayilar)


    
    
plaka_kodlari=[45,35,6,33,42]
yeni_plaka_kodlari=[i**2 for i in plaka_kodlari]
print(yeni_plaka_kodlari)

listem=[charecter for charecter in [1,2,3]]
print(listem)

aa=[ i for i in range (12) if i%2==0]
print (aa)

numbers =[-2,-7,-9,-10,-5,8,21,54]
positive_numbers=[ i for i in numbers if i>0]
print(numbers)

numbers=[1,6,4,5]
modified_numbers=[i*3 for i in numbers if i>5]
print (modified_numbers)

yy=["çift sayi" if i%2 ==0 else "tek sayi" for i in range(8)]
print (yy)

sicaklik=[32,100,40,212,]
donusturulmus_sicaklik=[(i-32)*5/9 if i>0 else i for i in sicaklik]
print (donusturulmus_sicaklik)

words=["apple","cat","banana","dog"]
modified_words=[word if len(word)>3 else "kısa kelime" for word in words]
print(modified_words)

notlar=[85,36,95,48,20]
harf_karsiliklari=["A" if nott>=90  else "B" if nott>=80 else "C" if nott>=70  else "D" for nott in notlar]
print(harf_karsiliklari)

names=["ibrahim","Firet"]
greetings=[ 'Mr.'+name[1:] if name[0] =="i" else 'Ms.'+name[1:] for name in names]
print(greetings)

#list comprehension with functions
def digitSum(n):
    dsum=0
    for ele in str(n):
        dsum+=int(ele)
        
    return dsum
    
    
list1=[367,562,945,111]
new_list1=[digitSum(i) for i in list1 if i%2!=0 ]
print(new_list1)


matris=[[j for j in range(3)] for i in range(5)]
print(matris)

#tektek harf alma
isim="MAKÜ BSM"
listem=[chr for chr in isim]
print(listem)


#lambda kullanımı
x=lambda a: a+10
print(x(5)) #15

x=lambda a:a*10
print(x(5)) #50

y=lambda a,b: a+b
print(y(3,4))

def math(n):
    return lambda a:a**n

kare=math(2)
print(kare(8))

küp=math(3)
print(küp(7))

#kare alma
even_numbers=[2,4,6,8,10,12]
squared_numbers=[ (lambda x:x**2 )(i)      for i in even_numbers]
print(squared_numbers)

words =["apple","cat","banana","dog"]
word_length=[ (lambda x:x+" "+ "kelimesi uzundur" if len(x) >3 else x +" "+"kelimesi kısadır") (i)    for i in words]
print(word_length)

#pythonda Map kullanımı
numbers=[1,2,3,4,5]
def square(num):
    return num**2
result=list(map(square,numbers))
print(result)

words=["phyton","words","ibrahim"]
buyuk_harf=list(map(str.upper,words))
print(buyuk_harf)

list1=[1,2,3,4,5]
list2=[6,7,8,9,0]
toplam_liste=list(map((lambda x1,x2:x1+x2),list1,list2))
print(toplam_liste)

sayilar=list(map((lambda x:x%2),[i for i in range(2,44)]))
print(sayilar)
#isim[0:2] ilk iki harfi alır
isimler=["elif","firet","ibrahim","top"]
bas_harf=[isim[0:2]  for isim in list(map(lambda x :x,isimler)) if len (isim)<4]
print(bas_harf)

list1=[10,20,5,15]
list2=[7,25,10,5]
cikar=[sonuc for sonuc in list(map(lambda x1,y1:x1-y1 ,list1,list2))if sonuc<0]
print(cikar)

#filter
   

seq=[0,1,2,3,4,5,6,0]
result=list(filter(lambda x:x%2!=0,seq))
print(result)

def is_multiple_of_3(num):
    return num%3==0
numbers=[1,2,3,4,5,6,7,8,9,10]
sonuc=list(filter(lambda x:is_multiple_of_3(x),numbers))
print(sonuc)

#asal
numbers=range(1,50)
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: 
            return False
        
    return True    

asal=list(filter (is_prime,numbers))
print(asal)