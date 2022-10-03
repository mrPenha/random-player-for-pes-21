import os
import random
os.system('clear')

posicao_registrada = random.choice(['Centroavante', 'Segundo atacante', 'Ponta esquerda', 'Ponta direita', 'Meia atacante', 'Meia esquerda',
                                    'Meia direita', 'Meia de ligação', 'Volante', 'Lateral esquerdo', 'Lateral direito', 'Zagueiro', 'Goleiro'])


def imprimir_posicao_registrada():
    print('*POSIÇÃO REGISTRADA* \n')
    print(f'{posicao_registrada}')


imprimir_posicao_registrada()
print()
