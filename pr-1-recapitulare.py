N = int(input("Introduceți un număr întreg: "))
p= 0
i= 0
while N > 0:
    cifra = N % 10  
    if cifra % 2 == 0:
        p+= 1
    else:
        i+= 1
    N//= 10  

print("Numărul de cifre pare este ", p)
print("Numărul de cifre impare este ",i)
