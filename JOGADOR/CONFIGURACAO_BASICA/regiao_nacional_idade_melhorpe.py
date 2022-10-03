import os
import random
os.system('clear')

regiao = random.choice(['Europa', 'Africa', 'América do norte',
                       'América central', 'América do sul', 'Ásia', 'Oceania'])

europa = [
    'ALBÂNIA',
    'ANDORRA',
    'ARMÊNIA',
    'ÁUSTRIA',
    'AZERBAIJÃO',
    'BIELORRÚSSIA',
    'BÉLGICA',
    'BÓSNIA E HERZEGOVINA',
    'BULGÁRIA',
    'CROÁCIA',
    'CHIPRE',
    'REPÚBLICA CHECA',
    'DINAMARCA',
    'INGLATERRA',
    'ESTÔNIA',
    'ILHAS FAROE',
    'FINLÂNDIA',
    'FRANÇA',
    'GEÓRGIA',
    'ALEMANHA',
    'GIBRALTAR',
    'GRÉCIA',
    'HUNGRIA',
    'ISLÂNDIA',
    'IRLANDA',
    'ISRAEL',
    'ITÁLIA',
    'CAZAQUISTÃO',
    'KOSOVO',
    'LETÔNIA',
    'LIECHTENSTEIN',
    'LITUÂNIA',
    'LUXEMBURGO',
    'MALTA',
    'MOLDÁVIA',
    'MONTENEGRO',
    'PAÍSES BAIXOS',
    'MACEDÓNIA DO NORTE',
    'IRLANDA DO NORTE',
    'NORUEGA',
    'POLÔNIA',
    'PORTUGAL',
    'ROMÊNIA',
    'RÚSSIA',
    'SÃO MARINO',
    'ESCÓCIA',
    'SÉRVIA',
    'ESLOVÁQUIA',
    'ESLOVÊNIA',
    'ESPANHA',
    'SUÉCIA',
    'SUÍÇA',
    'PERU',
    'UCRÂNIA',
    'GALES'
]

africa = [
    'ARGÉLIA',
    'BURKINA FASO',
    'CAMARÕES',
    'COSTA DO MARFIM',
    'EGITO',
    'GANA',
    'GUINÉ',
    'MALI',
    'MARROCOS',
    'NIGÉRIA',
    'SENEGAL',
    'ÁFRICA DO SUL',
    'TUNÍSIA',
    'ZÂMBIA'
]

america_norte = [
    'EUA',
    'MÉXICO'
]

america_central = [
    'COSTA RICA',
    'HONDURAS',
    'PANAMÁ',
    'JAMAICA'
]

america_sul = [
    'ARGENTINA',
    'BOLÍVIA',
    'BRASIL',
    'CHILE',
    'COLOMBIA',
    'EQUADOR',
    'PARAGUAI',
    'PERU',
    'URUGUAI',
    'VENEZUELA'
]

asia = [
    'CHINA',
    'IRÃ',
    'IRAQUE',
    'JAPÃO',
    'JORDÂNIA',
    'COREIA DO NORTE',
    'KUWAIT',
    'LÍBANO',
    'OMÃ',
    'COREIA DO SUL',
    'ARÁBIA SAUDITA',
    'TAILÂNDIA',
    'EMIRADOS ÁRABES UNIDOS',
    'UZBEQUISTÃO',
    'CATAR'
]

oceania = [
    'AUSTRÁLIA',
    'NOVA ZELÂNDIA'
]


#  nacionalidade
if regiao == 'Europa':
    nacionalidade = random.choice(europa)

elif regiao == 'Africa':
    nacionalidade = random.choice(africa)

elif regiao == 'América do norte':
    nacionalidade = random.choice(america_norte)

elif regiao == 'América central':
    nacionalidade = random.choice(america_central)

elif regiao == 'América do sul':
    nacionalidade = random.choice(america_sul)

elif regiao == 'Ásia':
    nacionalidade = random.choice(asia)

elif regiao == 'Oceania':
    nacionalidade = random.choice(oceania)

else:
    pass

#  idade
idade = random.randint(15, 50)


#  melhor pé
pe = random.choice(['Pé direito', 'Pé esquerdo'])


def imprimir_configuracao_basica():
    print('*CONFIGURAÇÃO BÁSICA* \n')
    print(f'Nacionalidade ______ {nacionalidade} ')
    print(f'Idade ______________ {idade} ')
    print(f'Melhor pé __________ {pe} \n\n')


imprimir_configuracao_basica()
