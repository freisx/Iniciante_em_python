print ("Fatorial de um numero!")
num = int(input("Digite o número:"))
fatorial = 1

for n in range(1, num + 1):
    fatorial *= n

print (fatorial)