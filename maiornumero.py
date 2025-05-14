print ("adivinhar o maior número.")
#variavel de numero pequeno.
maior = float('-inf')

#laço de repetição para guardar as variaveis.
for n in range(1,6):
    numero= int(input(f"Digite o {n} número:"))
    if numero > maior:
        maior = numero

print(f"Esse é o maior número: {maior}")