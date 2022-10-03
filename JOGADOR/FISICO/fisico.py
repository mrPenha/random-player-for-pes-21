from http.client import ImproperConnectionState


import os
import random
os.system('clear')

altura = random.randint(155, 210)
peso = random.randint(30, 129)

const_fisica = []
for i in range(11):
    aleatorio = random.randint(-7, 7)
    for j in range(1):
        const_fisica.append(aleatorio)

for i in range(len(const_fisica)):
    if const_fisica[i] >= 0:
        const_fisica[i] = f'{const_fisica[i]:+}'


def imprimir_fisico():
    print('*FÍSICO* \n\n')
    print(f'Altura(cm) ----------------- {altura}')
    print(f'Peso(kg) ------------------- {peso}')
    print(f'Altura do pescoço ---------- {const_fisica[0]}')
    print(f'Largura do pescoço --------- {const_fisica[1]}')
    print(f'Altura dos ombros ---------- {const_fisica[2]}')
    print(f'Largura dos ombros --------- {const_fisica[3]}')
    print(f'Medida do peito ------------ {const_fisica[4]}')
    print(f'Cintura -------------------- {const_fisica[5]}')
    print(f'Largura do braço ----------- {const_fisica[6]}')
    print(f'Coxas ---------------------- {const_fisica[7]}')
    print(f'Panturrilhas --------------- {const_fisica[8]}')
    print(f'Comp. das pernas ----------- {const_fisica[9]}')
    print(f'Comp. dos braços ----------- {const_fisica[10]}')


imprimir_fisico()
