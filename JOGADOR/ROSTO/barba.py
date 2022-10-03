import os
import random
os.system('clear')

#  estilo da barba
estilo = random.randint(0, 19)

#  cor editada
cor_R = random.randint(0, 63)
cor_G = random.randint(0, 63)
cor_B = random.randint(0, 63)

#  volume da barba
volume = random.randint(0, 3)


def imprimir_barba():
    print('*BARBA* \n')
    if estilo == 0:
        print(f'Estilo da barba __________ Desl. ')
        print(f'Cor da barba _____________ Desl. ')
        print(f'Volume da barba __________ Desl. ')

    else:
        print(f'Estilo da barba __________ {estilo} ')
        print(f'Cor da barba _____________ R:{cor_R} / G:{cor_G} / B:{cor_B} ')
        print(f'Volume da barba __________ {volume} ')


imprimir_barba()
print()
