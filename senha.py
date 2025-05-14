print("Tente advinhar a senha!")
tentativa = str (input("Digite a senha:"))
senha = str("gui123")

while tentativa != senha:
    print("Acesso Negado. \n Tente Novamente.")
    tentativa = str (input("Digite a senha:"))

print("Acesso Permitido")