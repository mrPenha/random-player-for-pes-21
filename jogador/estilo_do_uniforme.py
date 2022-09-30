import os
import random
os.system('clear')

#  chuteiras
chuteiras = random.randint(1, 70)

#  bandagem
munhequeiras = ['Desligado', 'Direita', 'Esquerda', 'Ambos']
m = munhequeiras[random.randint(0, 3)]

cor_das_munhequeiras = ['Cor do uniforme', 'Branco', 'Preto', 'Bege']
cm = cor_das_munhequeiras[random.randint(0, 3)]

tornozeleiras = ['Desligada', 'Ligada']
t = tornozeleiras[random.randint(0, 1)]

#  luvas do jogador
luvas_do_jogador = ['Desligado', 'Usa no inverno']
l = luvas_do_jogador[random.randint(0, 1)]

cor_do_uniforme = ['Branco', 'Preto', 'Vermelho',
                   'Azul-Escuro', 'Amarelo', 'Verde', 'Rosa', 'Azul-Claro']
c = cor_do_uniforme[random.randint(0, 7)]


def imprimir_chuteira():
    print('*CHUTEIRA* \n')
    print(f'Chuteira                 {chuteiras}')


def imprimir_bandagem():
    if m == munhequeiras[0]:
        print('*BANDAGEM* \n')
        print(f'Munhequeiras             {m}')
        print(f'Cor das Munhequeiras     -')
        print(f'Tornozeleiras            {t}')

    else:
        print('*BRANDAGEM* \n')
        print(f'Munhequeiras             {m}')
        print(f'Cor das Munhequeiras     {cm}')
        print(f'Tornozeleiras            {t}')


def imprimir_luvas_do_jogador():
    if l == luvas_do_jogador[0]:
        print('*COR* \n')
        print(f'Luvas do Jogador         {l}')
        print(f'Cor                      -')

    else:
        print('*COR* \n')
        print(f'Luvas do Jogador          {l}')
        print(f'Cor                       {c}')


imprimir_chuteira()
print('---------------------------------------- \n')
imprimir_bandagem()
print('---------------------------------------- \n')
imprimir_luvas_do_jogador()
print('---------------------------------------- \n')
