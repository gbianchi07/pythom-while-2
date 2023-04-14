cont=1
numero = int(input('numero: '))
menor= numero
while cont <= 9 :
    numero = int(input('numero: '))
    if numero < menor:
        menor = numero
    cont += 1
print(f'menor numero é {menor}')