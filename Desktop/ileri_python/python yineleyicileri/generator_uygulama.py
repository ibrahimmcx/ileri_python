#1-sonsuz aralığındaki her sayının karesini getiren fonksiyon
#fibonacci serisini hem normal fpnksiyon hemde generator fonk ile oluştur
#performans testlerini yap

# def sayi_uret():
#     sayi=0
#     while True:
#         yield sayi**2
#         sayi+=1
# generator=sayi_uret()
# print(next(generator))


def fib_list(max):
    sayilar=[]
    a,b=0,1
    while len(sayilar)<max:
        sayilar.append(b)
        a,b=b,a+b


    return sayilar
print(fib_list(10))

def fib_gen(max):
    a,b=0,1
    count=0
    while count <=max:
        a,b=b,a+b
        yield b
        count +=1
import sys
liste=[i for i in range(100)]
print(sys.getsizeof)        

gen=(i for i in range(100))
print(sys.getsizeof(gen))  