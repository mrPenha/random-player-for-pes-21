import os
import random
os.system('clear')

jogador_de_linha = []
for i in range(20):
    aleatorio = random.randint(40, 99)
    for j in range(1):
        jogador_de_linha.append(aleatorio)

goleiro = []
for i in range(5):
    aleatorio = random.randint(40, 99)
    for j in range(1):
        goleiro.append(aleatorio)

pior_pe_freq = random.randint(1, 4)
pior_pe_prec = random.randint(1, 4)
forma_fisica = random.randint(1, 8)
resistencia_lesao = random.randint(1, 3)


def imprimir_habilidades_jogador_de_linha():
    print('*JOGADOR DE LINHA* \n')
    # if posicao_registrada is not GO:
    print(f'Talento ofensivo ___________ {jogador_de_linha[0]} ')
    print(f'Controle de bola ___________ {jogador_de_linha[1]} ')
    print(f'Drible _____________________ {jogador_de_linha[2]} ')
    print(f'Condução firme _____________ {jogador_de_linha[3]} ')
    print(f'Passe rasteiro _____________ {jogador_de_linha[4]} ')
    print(f'Passe alto _________________ {jogador_de_linha[5]} ')
    print(f'Finalização ________________ {jogador_de_linha[6]} ')
    print(f'Cabeceio ___________________ {jogador_de_linha[7]} ')
    print(f'Chute Colocado _____________ {jogador_de_linha[8]} ')
    print(f'Curva ______________________ {jogador_de_linha[9]} ')
    print(f'Velocidade _________________ {jogador_de_linha[10]} ')
    print(f'Aceleração _________________ {jogador_de_linha[11]} ')
    print(f'Força do chute _____________ {jogador_de_linha[12]} ')
    print(f'Impulsão ___________________ {jogador_de_linha[13]} ')
    print(f'Contato físico _____________ {jogador_de_linha[14]} ')
    print(f'Equilíbrio _________________ {jogador_de_linha[15]} ')
    print(f'Resistência ________________ {jogador_de_linha[16]} ')
    print(f'Talento defensivo __________ {jogador_de_linha[17]} ')
    print(f'Desarme ____________________ {jogador_de_linha[18]} ')
    print(f'Agressividade ______________ {jogador_de_linha[19]} ')
    print(f'Talento de GO ______________ 40 ')
    print(f'Firmeza do GO ______________ 40 ')
    print(f'Afast. de bola do GO _______ 40 ')
    print(f'Reflexos do GO _____________ 40 ')
    print(f'Alcance do GO ______________ 40 ')
    print(f'Pior pé (frequência) _______ {pior_pe_freq} ')
    print(f'Pior pé (precisão) _________ {pior_pe_prec} ')
    print(f'Forma física _______________ {forma_fisica} ')
    print(f'Resistência a lesão ________ {resistencia_lesao} ')

    # else:
    print(f'Talento ofensivo ___________ {jogador_de_linha[0]} ')
    print(f'Controle de bola ___________ {jogador_de_linha[1]} ')
    print(f'Drible _____________________ {jogador_de_linha[2]} ')
    print(f'Condução firme _____________ {jogador_de_linha[3]} ')
    print(f'Passe rasteiro _____________ {jogador_de_linha[4]} ')
    print(f'Passe alto _________________ {jogador_de_linha[5]} ')
    print(f'Finalização ________________ {jogador_de_linha[6]} ')
    print(f'Cabeceio ___________________ {jogador_de_linha[7]} ')
    print(f'Chute Colocado _____________ {jogador_de_linha[8]} ')
    print(f'Curva ______________________ {jogador_de_linha[9]} ')
    print(f'Velocidade _________________ {jogador_de_linha[10]} ')
    print(f'Aceleração _________________ {jogador_de_linha[11]} ')
    print(f'Força do chute _____________ {jogador_de_linha[12]} ')
    print(f'Impulsão ___________________ {jogador_de_linha[13]} ')
    print(f'Contato físico _____________ {jogador_de_linha[14]} ')
    print(f'Equilíbrio _________________ {jogador_de_linha[15]} ')
    print(f'Resistência ________________ {jogador_de_linha[16]} ')
    print(f'Talento defensivo __________ {jogador_de_linha[17]} ')
    print(f'Desarme ____________________ {jogador_de_linha[18]} ')
    print(f'Agressividade ______________ {jogador_de_linha[19]} ')
    print(f'Talento de GO ______________ {goleiro[0]} ')
    print(f'Firmeza do GO ______________ {goleiro[0]} ')
    print(f'Afast. de bola do GO _______ {goleiro[0]} ')
    print(f'Reflexos do GO _____________ {goleiro[0]} ')
    print(f'Alcance do GO ______________ {goleiro[0]} ')
    print(f'Pior pé (frequência) _______ {pior_pe_freq} ')
    print(f'Pior pé (precisão) _________ {pior_pe_prec} ')
    print(f'Forma física _______________ {forma_fisica} ')
    print(f'Resistência a lesão ________ {resistencia_lesao} ')


imprimir_habilidades_jogador_de_linha()
print()
