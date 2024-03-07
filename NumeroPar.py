class ErroImpar(Exception):
    pass
try:
    numero = int(input("Digite um número inteiro: "))
    divisao = numero % 2 
    if divisao != 0:
        raise ErroImpar ("Número Impar!")
except ErroImpar as e:
    print(e)
else:
    print("Número Par!")
    