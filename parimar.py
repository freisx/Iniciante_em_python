print("Par ou Impar.\n O programa para ao digitar 0.")

while True:
    num = int(input("Digite um número para a verificação."))
    if num == 0:
        break
    elif num % 2 == 0:
        print("Esse número é par!")
    else:
        print ("Esse número é impar!")

print("Encerrado!")