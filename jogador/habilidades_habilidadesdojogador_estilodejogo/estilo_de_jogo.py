import os
import random
os.system('clear')

estilo = random.choice([
    'Artilheiro',
    'Puxa marcação',
    'Homem de área',
    'Pivô',
    'Armador criativo',
    'Ala produtivo',
    'Lateral móvel',
    'Especialista em cruz.',
    'Clássica nº 10',
    'Jog. de infiltração',
    'Meia versátil',
    'O destruidor',
    'Orquestrador',
    'Primeiro volante',
    'Zagueiro ofensivo',
    'Lateral atacante',
    'Zagueiro defensivo',
    'Provocador',
    'Atacante surpresa',
    'Goleiro ofensivo',
    'Goleiro defensivo'
])


def imprimir_estilo_de_jogo():
    print('*ESTILO DE JOGO* \n')
    print(f'{estilo}')


imprimir_estilo_de_jogo()
print()
