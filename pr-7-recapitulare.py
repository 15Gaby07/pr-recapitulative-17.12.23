n = int(input("Introdu numărul de numere: "))
n_nenorocoase = 0

for i in range(n):
    num = input('N: ')
    if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]) and int(num[0]) + int(num[1]) == 13:
        n_nenorocoase+= 1

print(n_nenorocoase)
