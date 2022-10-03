import os
import random
os.system('clear')

tipo_lab_superior = random.randint(1, 5)
tipo_lab_inferior = random.randint(1, 5)

lista = []
for i in range(5):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        lista.append(aleatorio)

for i in range(len(lista)):
    if lista[i] >= 0:
        lista[i] = f'{lista[i]:+}'
    else:
        pass


def imprimir_boca():
    print('*BOCA* \n')
    print(f'Tipo lábio sup. ___________ {tipo_lab_superior} ')
    print(f'Tipo lábio inf. ___________ {tipo_lab_inferior} ')
    print(f'Posição da boca ___________ {lista[0]} ')
    print(f'Tam. dos lábios ___________ {lista[1]} ')
    print(f'Largura do lábio __________ {lista[2]} ')
    print(f'Formato da boca ___________ {lista[3]} ')
    print(f'Profund. da boca __________ {lista[4]} ')


imprimir_boca()
print()
