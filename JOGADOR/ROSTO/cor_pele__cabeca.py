import os
import random
os.system('clear')

cor = random.randint(1, 6)

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


def imprimir_cc():
    print('*PROP. DA COR DA PELE / CABEÇA* \n')
    print(f'Cor da pele (1 até 6) __________  {cor} ')
    print(f'Altura da cabeça _______________ {lista[0]} ')
    print(f'Largura da cabeça ______________ {lista[1]} ')
    print(f'Profun. da cabeça ______________ {lista[2]} ')
    print(f'Altura do rosto ________________ {lista[3]} ')
    print(f'Tamanho do rosto _______________ {lista[4]} ')


imprimir_cc()
print()
