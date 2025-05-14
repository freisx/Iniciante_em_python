print ("Adivinhe!")
import random

secreto = random.randint(1,10)
palpite = -1


while palpite != secreto:
    palpite = int(input ("Tente adivinhar o numero de 1 a 10:"))
    if palpite != secreto:
        print("Você errou, Tente novamente!")

print("Parabéns, esse era o número certo:", secreto)