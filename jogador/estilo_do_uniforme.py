import os
import random
os.system('clear')

#  chuteiras
chuteiras = random.randint(1, 70)

#  bandagem
munhequeiras = random.choice(['Desligado', 'Direita', 'Esquerda', 'Ambos'])

cor_das_munhequeiras = random.choice(
    ['Cor do uniforme', 'Branco', 'Preto', 'Bege'])

tornozeleiras = random.choice(['Desligada', 'Ligada'])

#  luvas do jogador
luvas_do_jogador = random.choice(['Desligado', 'Usa no inverno'])

cor_da_luva = random.choice(
    ['Branco', 'Preto', 'Vermelho', 'Azul-Escuro', 'Amarelo', 'Verde', 'Rosa', 'Azul-Claro'])


#  luvas do goleiro
luvas_do_goleiro = random.randint(1, 11)

#  roupa de baixo
roupa_de_baixo = random.choice(['Verão: Desl./Inverno: Desl.', 'Verão: Desl./Inverno: Longo.',
                               'Verão: Curto./Inverno: Curto.', 'Verão: Curto./Inverno: Longo.'])

#  mangas
mangas = random.choice(['Curto', 'Longo', 'Verão: Curto / Inverno: Longo'])

#  extremidade da camisa
extremidade_camisa = random.choice(['Por dentro', 'Por Fora'])

#  comprimento da meia
comprimento_meia = random.choice(['Padrão', 'Longo', 'Curto'])

#  camisetas internas
camisetas_internas = random.choice(['Desligado', 'Normal', 'Gola rolê'])


def imprimir_estilo_uniforme():
    print('*ESTILO DO UNIFORME* \n\n')
    #  chuteiras
    print(f'CHUTEIRAS \n')
    print(f'Modelo ------------------------- {chuteiras} \n\n')

    #  bandagens
    print(f'BANDAGEM \n')
    if munhequeiras != 'Desligado':
        print(f'Munhequeiras ------------------- {munhequeiras} \n')
        print(f'Cor das Munhequeiras ----------- {cor_das_munhequeiras} \n')
        print(f'Tornozeleiras ------------------ {tornozeleiras} \n\n')
    else:
        print(f'Munhequeiras ------------------- {munhequeiras} \n')
        print(f'Cor das Munhequeiras ----------- {munhequeiras} \n')
        print(f'Tornozeleiras ------------------ {tornozeleiras} \n\n')

    if luvas_do_jogador != 'Desligado':
        print(f'LUVAS DO JOGADOR \n')
        print(f'Modelo ------------------------- {luvas_do_jogador} \n')
        print(f'Cor ---------------------------- {cor_da_luva} \n\n')
    else:
        print(f'LUVAS DO JOGADOR \n')
        print(f'Modelo ------------------------- {luvas_do_jogador} \n\n')

    #  luvas do goleiro se posição registrada == goleiro
    print(f'LUVAS DO GOLEIRO \n')
    print(f'Modelo ------------------------- {luvas_do_goleiro} \n\n')

    print(f'ROUPA DE BAIXO \n')
    print(f'Verão / Inverno ---------------- {roupa_de_baixo} \n\n')

    #  mangas
    print(f'MANGAS \n')
    print(f'Verão / Inverno ---------------- {mangas} \n\n')

    #  extremidade da camisa
    print(f'EXTREMIDADE DA CAMISA \n')
    print(f'Extremidade -------------------- {extremidade_camisa} \n\n')

    #  comprimento da meia
    print(f'COMPRIMENTO DA MEIA \n')
    print(f'comprimento -------------------- {comprimento_meia} \n\n')

    #  camisetas internas
    print(f'CAMISETAS INTERNAS \n')
    print(f'Camisetas ---------------------- {camisetas_internas} \n\n')


imprimir_estilo_uniforme()
