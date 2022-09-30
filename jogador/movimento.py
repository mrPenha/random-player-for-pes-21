import os
import random
os.system('clear')

drible_costas = random.randint(1, 5)
drible_braços = random.randint(1, 10)
corrida_costas = random.randint(1, 5)
corrida_braços = random.randint(1, 10)
chute_escanteio = random.randint(1, 10)
chute_falta = random.randint(1, 20)
chute_penalti = random.randint(1, 7)
celebracao_gol_1 = random.randint(0, 162)
celebracao_gol_2 = random.randint(0, 162)


def imprimir_movimento():

    print('*MOVIMENTO*\n')
    print('Drible\n')

    print(f'Curv. das costas          {drible_costas}')
    print(f'Curv. das costas          {drible_braços}')
    print('---------------------------- \n')

    print('Movim. de braços \n')
    print(f'Curv. das costas          {corrida_costas}')
    print(f'Curv. das costas          {corrida_braços}')
    print('---------------------------- \n')

    print('Movim. de chute \n')
    print(f'Curv. das costas          {chute_escanteio}')
    print(f'Curv. das costas          {chute_falta}')
    print(f'Curv. das costas          {chute_penalti}')
    print('---------------------------- \n')

    print('Celebração de gol \n')
    print(f'Curv. das costas          {celebracao_gol_1}')
    print(f'Curv. das costas          {celebracao_gol_2}')
    print('---------------------------- \n')


imprimir_movimento()
