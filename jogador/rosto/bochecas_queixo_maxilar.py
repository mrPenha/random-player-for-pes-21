import os
import random
os.system('clear')

tipo_rosto = random.randint(1, 6)
tipo_papo = random.randint(1, 4)

lista = []
for i in range(6):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        lista.append(aleatorio)

for i in range(len(lista)):
    if lista[i] >= 0:
        lista[i] = f'{lista[i]:+}'
    else:
        pass


def imprimir_bqm():
    print('*BOCHECHAS / QUEIXO / MAXILAR* \n')
    print(f'Tipo de rosto _______________  {tipo_rosto} ')
    print(f'Tipo de papo ________________  {tipo_papo} ')
    print(f'Maçãs do rosto ______________ {lista[0]} ')
    print(f'Altura do queixo ____________ {lista[1]} ')
    print(f'Largura do queixo ___________ {lista[2]} ')
    print(f'Altura do maxilar ___________ {lista[3]} ')
    print(f'Largura do maxilar __________ {lista[4]} ')
    print(f'Profund. do queixo __________ {lista[5]} ')


imprimir_bqm()
print()
