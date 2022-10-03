import os
import random
os.system('clear')

habilidades = [
    'Pedalada simples',
    'Toque duplo',
    'Elástico',
    '360 graus',
    'Chapéu',
    'Corte de calcanhar',
    'Puxada de letra',
    'Finta de letra',
    'Controle de domínio',
    'Cabeçada',
    'Chute de longe',
    'Controle de cavadinha',
    'Precisão a distância',
    'Chute com o peito do pé',
    'Folha seca',
    'Chute Ascendente',
    'Finaliz. acrobática',
    'Toque de calcanhar',
    'Chute de primeira',
    'Passe de primeira',
    'Passe em profundidade',
    'Passe na medida',
    'Cruzamento preciso',
    'Cruva pra fora',
    'De letra',
    'Passe sem olhar',
    'Passe aéreo baixo',
    'Repos. baixa do GO',
    'Repos. alta do GO',
    'Arem. lateral longo',
    'Arrem. longo do GO',
    'Especialista em pênalti',
    'Pegador de pênaltis',
    'Malícia',
    'Marcação individual',
    'Volta para marcar',
    'Interceptação',
    'Afastamento acrobático',
    'Liderança',
    'Super Substituto',
    'Espirito guerreiro'
]

qtd = random.randint(0, 10)

lista = []
if qtd > 0:
    for i in range(qtd):
        aleatorio = random.choice(habilidades)
        if aleatorio not in lista:
            lista.append(aleatorio)
        else:
            pass


def imprimir_habilidades_do_jogador():
    for i in range(len(lista)):
        print(lista[i])


print('*HABILIDADES DO JOGADOR* \n')
imprimir_habilidades_do_jogador()
print()
