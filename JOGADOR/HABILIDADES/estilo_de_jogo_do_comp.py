import os
import random
os.system('clear')

estilo = [
    'Malandro',
    'Drible veloz',
    'Rápido como uma bala',
    'Corrida com gás',
    'Perito em bola longa',
    'Cruz. antecip.',
    'Batedor Pro'
]

qtd = random.randint(0, 5)

lista = []
if qtd > 0:
    for i in range(qtd):
        aleatorio = random.choice(estilo)
        if aleatorio not in lista:
            lista.append(aleatorio)
        else:
            pass


def imprimir_estilo_de_jogo_comp():
    for i in range(len(lista)):
        print(lista[i])


print('*ESTILOS DE JOGO DO COMP* \n')
imprimir_estilo_de_jogo_comp()
print()
