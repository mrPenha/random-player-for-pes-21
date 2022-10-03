import os
import random
os.system('clear')

tipo_superior = random.randint(1, 8)
tipo_inferior = random.randint(1, 7)
cor = random.randint(1, 11)

lista = []
for i in range(13):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        lista.append(aleatorio)

for i in range(len(lista)):
    if lista[i] >= 0:
        lista[i] = f'{lista[i]:+}'
    else:
        pass


def imprimir_olhos():
    print('*OLHOS* \n')
    print(f'Tipo de pálp. superior ___________________  {tipo_superior} ')
    print(f'Tipo de pálp. inferior ___________________  {tipo_inferior} ')
    print(f'Altura do olho ___________________________ {lista[0]} ')
    print(f'Posição horiz. do olho ___________________ {lista[1]} ')
    print(f'Cor dos olhos (0 até 11) _________________  {cor} ')
    print(f'Tamanho da pupila ________________________ {lista[2]} ')
    print(f'Altura da Pálp. superior(int.) ___________ {lista[3]} ')
    print(f'Largura da Pálp. superior(int.) __________ {lista[4]} ')
    print(f'Altura da Pálp. superior(ext.) ___________ {lista[5]} ')
    print(f'Largura da Pálp. superior(ext.) __________ {lista[6]} ')
    print(f'Alt. do int. do olho _____________________ {lista[7]} ')
    print(f'Pos. canto int. do olho __________________ {lista[8]} ')
    print(f'Alt. do ext. do olho _____________________ {lista[9]} ')
    print(f'Pos. canto ext. do olho __________________ {lista[10]} ')
    print(f'Altura das olheiras ______________________ {lista[11]} ')
    print(f'Profundidade do olho _____________________ {lista[12]} ')


imprimir_olhos()
print()
