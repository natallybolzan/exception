class TamanhoPalavra(Exception):
    pass
try:
    palavra1 = input("Digite a primeira palavra:\n")
    palavra2 = input("Digite a segunda palavra:\n")
    if len(palavra1)!= len(palavra2):
        raise TamanhoPalavra("O Comprimento das duas palavras é diferente.")
except TamanhoPalavra as t:
    print(t)
else:
    print("O Comprimento das duas palavras é igual.")