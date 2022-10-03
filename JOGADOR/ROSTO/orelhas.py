import os
import random
os.system('clear')


lista = []
for i in range(3):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        lista.append(aleatorio)

for i in range(len(lista)):
    if lista[i] >= 0:
        lista[i] = f'{lista[i]:+}'
    else:
        pass


def imprimir_orelha():
    print('*ORELHAS*\n')
    print(f'Comp. da orelha ___________ {lista[0]}')
    print(f'Larg. da orelha ___________ {lista[1]}')
    print(f'Ângulo da orelha __________ {lista[2]}')


imprimir_orelha()
print()
