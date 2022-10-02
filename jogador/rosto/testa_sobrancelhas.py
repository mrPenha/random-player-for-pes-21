import os
import random
os.system('clear')

rugas = random.randint(1, 7)
tipo = random.randint(1, 8)
espessura = random.randint(0, 2)
estilo = random.choice(['Fina', 'Normal', 'Espessa'])
densidade = random.randint(0, 3)
cor = 'Igual à cor do cabelo'

if espessura or densidade >= 0:
    espessura = f'{espessura:+}'
    densidade = f'{densidade:+}'

lista = []
for i in range(5):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        lista.append(aleatorio)

for i in range(len(lista)):
    if lista[i] >= 0:
        lista[i] = f'{lista[i]:+}'
    else:
        pass


def imprimir_ts():
    print('*TESTA / SOBRANCELHAS* \n')
    print(f'Rugas na testa ___________________  {rugas} ')
    print(f'Tipo de sobrancelha ______________  {tipo} ')
    print(f'Sobrancelha (espes.) _____________  {espessura} ')
    print(f'estilo sobrancelha _______________ {estilo} ')
    print(f'Dens. da sobrancelha _____________ {densidade} ')
    print(f'Sobrancelha (cor) ________________ {cor} ')
    print(f'Ângulo da sobr.(int.) ____________ {lista[0]} ')
    print(f'Largura da glabela _______________ {lista[1]} ')
    print(f'Ângulo da sobr.(ext.) ____________ {lista[2]} ')
    print(f'Larg. da têmp. ___________________ {lista[3]} ')
    print(f'Profund. da sobrancelha __________ {lista[4]} ')


imprimir_ts()
print()
