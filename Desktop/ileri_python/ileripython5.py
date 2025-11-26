def is_pal_recursive(s,i=0,j=None):
    if j is None:
        j =len(s)-1
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False

    return is_pal_recursive(s,i+1,j-1)
print(is_pal_recursive("recacal"))
print(is_pal_recursive("aba"))    



def sum_digits(n:int)->int:
    n =abs(n)
    if n<10:
        return n
    return (n%10)+sum_digits(n//10) 
print(sum_digits(102))

#ıterator   