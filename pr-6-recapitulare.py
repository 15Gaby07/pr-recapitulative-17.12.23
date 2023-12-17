n = int(input("Introdu nr de numere "))
n_norocoase=0

for i in range(n):
    num = input("N: ")
    if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
        n_norocoase+= 1

print(n_norocoase)