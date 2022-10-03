import os
import random
os.system('clear')

tipo = random.randint(1, 8)
rugas = random.randint(1, 5)

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


def imprimir_nariz():
    print('*NARIZ* \n')
    print(f'Tipo de nariz _________________ {tipo} ')
    print(f'Rugas _________________________ {rugas} ')
    print(f'Altura do nariz _______________ {lista[0]} ')
    print(f'Largura da narina _____________ {lista[1]} ')
    print(f'Largura do nariz ______________ {lista[2]} ')
    print(f'Comprimento do nariz __________ {lista[3]} ')
    print(f'Prof. do nariz ________________ {lista[4]} ')


imprimir_nariz()
print()
