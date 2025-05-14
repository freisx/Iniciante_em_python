print ("tabuada.")
num = int(input("digite um numero de 1 a 10:"))
mult = 0

if num <=10:
    for n in range(1, 11):
        mult = n * num
        print(n, "x", num, "=", mult)
else:
    print("número inválido.")
