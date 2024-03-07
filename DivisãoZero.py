D = int(input("Digite um divisor: "))

if D == 0:
    try:
        divisao = 10/ 0
    except ZeroDivisionError:
        print("Valor indeterminado!\nDivisão por zero.") 
else:
    divisao = 10/ D
    print("Resultado: ",divisao)