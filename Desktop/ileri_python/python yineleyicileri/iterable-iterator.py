sayilar=[1,2,3,4,5,6]
iterator=iter(sayilar)
print(next(iterator)) #1 tane olduğu için ilk elemanı yazdırır.

while True:
    try:
        sayi=next(iterator)
        print(sayi)
    except StopIteration:
        break    