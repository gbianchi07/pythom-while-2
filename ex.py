cont=1                #contador
soma = 0              #somador
while cont <= 15:
    numero = int(input('numero: '))
    if numero % 2 != 0:
        soma += numero
    cont += 1

print(f'somatorio dos impares {soma}')

