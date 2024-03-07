palavra = input("Digite uma palavra:\n")

if any(x.isupper() for x in palavra):
     print('Sua palavra contêm letras Maiúsculas.')
else:
     class LetraMaiúscula(Exception):
          pass
     try:
          
          raise LetraMaiúscula("Sua palavra contêm letras Minúsculas.")
     except LetraMaiúscula as l:
          print(l)