import time

print("Apenas números pares de 1 a 100!")

for n in range(1, 101):
    if n % 2 == 0:
        print(n)
        time.sleep(1)