import os
import random
from posicao_registrada import posicao_registrada
os.system('clear')

qtd = random.randint(1, 12)

lista_posicao = []
lista_afinidade = []

if posicao_registrada != 'Goleiro':
    for i in range(qtd):
        posicao_jogavel = random.choice(['CA', 'SA', 'PTE', 'PTD', 'MAT',
                                        'MLE', 'MLD', 'MLG', 'VOL', 'LE', 'LD', 'ZC'])

        afinidade = random.choice(['A', 'B', 'C'])

        for j in range(1):
            if posicao_jogavel not in lista_posicao:
                lista_posicao.append(posicao_jogavel)
                lista_afinidade.append(afinidade)
            else:
                pass
else:
    posicao_jogavel = ['GO']
    afinidade = ['A']


def imprimir_posicao_jogavel():
    print('*POSIÇÃO JOGÁVEL* \n')
    for i in range(len(lista_posicao)):
        print(f'Posição ______ {lista_posicao[i]}')
        print(f'Afinidade ____ {lista_afinidade[i]} \n')


imprimir_posicao_jogavel()
