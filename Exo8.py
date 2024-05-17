#Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). 

s = "Ayiti kapab avanse"
total = 0

for i in range(len(s)):
    if s[i].lower() == 'a' :  
        total += i

print(total)