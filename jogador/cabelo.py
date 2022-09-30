import os
import random
os.system('clear')

#  GERAL
estilo_g = random.choice(['Especial', 'Normal', 'Seco',
                         'Moicano', 'Black Power', 'Dreadlocks', 'Tranças'])
# se comprimento ==raspado, anula tudo, exceto nivel de cachos
comprimento_g = random.choice(
    ['Raspado', 'Muito Curto', 'Curto', 'Médio', 'Longo'])
nivel_cachos_g = random.randint(0, 6)
# somente para o estilo especial
variacao_cabelo_g = random.randint(1, 29)


#  FRENTE
estilo_f = random.choice(['Cima', 'Baixo', 'Pent. pra trás'])
partido_f = random.choice(
    ['Desligado', 'Esquerda 2', 'Esquerda 1', 'Centro', 'Direita 2', 'Direita 1'])
linha_cabelo_f = random.randint(1, 3)
larg_testa_f = random.choice(['Normal', 'Larga', 'Estreita'])


#  LADOS/ATRÁS
estilo_la = random.choice(
    ['Raspado', 'Normal', 'Reduzir' 'volume', 'Lados menores'])
raspado = random.randint(1, 6)


#  COR DO CABELO/ACESSÓRIO
# cor do cabelo editado RGB
cor_cabelo_R = random.randint(0, 63)
cor_cabelo_G = random.randint(0, 63)
cor_cabelo_B = random.randint(0, 63)
acessorio = random.choice(['Ligado', 'Desligado'])
cor_acessorio = random.choice(
    ['Branco', 'Preto', 'Vermelhor', 'Azul-escuro', 'Amarelo', 'Verde', 'Rosa', 'Azul-claro'])


def imprimir_cabelo():
    print('*CABELO* \n')

    #  RASPADO
    if comprimento_g == 'Raspado':
        print(f'Estilo __________________________ --- ')
        print(f'Comprimento _____________________ {comprimento_g} ')
        print(f'Nível de cachos _________________ {nivel_cachos_g} ')
        print(f'Variação do cabelo ______________ --- ')
        print(f'Estilo frente ___________________ --- ')
        print(f'Partido frente __________________ --- ')
        print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
        print(f'Largura da testa ________________ {larg_testa_f} ')
        print(f'Estilo lados/trás _______________ --- ')
        print(f'Raspado lados/trás ______________ {raspado} ')
        print(
            f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
        print(f'Acessórios ______________________ --- ')
        print(f'Cor do acessório ________________ --- ')

    else:

        #  ESPECIAL
        if estilo_g == 'Especial':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ --- ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ {variacao_cabelo_g} ')
            print(f'Estilo frente ___________________ --- ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ --- ')
            print(f'Largura da testa ________________ --- ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        #  NORMAL
        elif estilo_g == 'Normal' and comprimento_g == 'Muito Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Normal' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Normal' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Normal' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        #  SECO
        elif estilo_g == 'Seco' and comprimento_g == 'Muito Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Seco' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Seco' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Seco' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ {partido_f} ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        #  MOICANO
        elif estilo_g == 'Moicano' and comprimento_g == 'Muito Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Moicano' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Moicano' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Moicano' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ {nivel_cachos_g} ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        #  BLACK POWER
        elif estilo_g == 'Black Power' and comprimento_g == 'Muito curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Black Power' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Black Power' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Black Power' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        #  DREADLOCKS
        elif estilo_g == 'Dreadlocks' and comprimento_g == 'Muito curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Dreadlocks' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Dreadlocks' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Dreadlocks' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        #  TRANÇAS
        elif estilo_g == 'Tranças' and comprimento_g == 'Muito curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ --- ')
            print(f'Raspado lados/trás ______________ {raspado} ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Tranças' and comprimento_g == 'Curto':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ --- ')
            print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Tranças' and comprimento_g == 'Médio':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        elif estilo_g == 'Tranças' and comprimento_g == 'Longo':
            print(f'Estilo __________________________ {estilo_g} ')
            print(f'Comprimento _____________________ {comprimento_g} ')
            print(f'Nível de cachos _________________ --- ')
            print(f'Variação do cabelo ______________ --- ')
            print(f'Estilo frente ___________________ {estilo_f} ')
            print(f'Partido frente __________________ --- ')
            print(f'Linha do cabelo _________________ {linha_cabelo_f} ')
            print(f'Largura da testa ________________ {larg_testa_f} ')
            print(f'Estilo lados/trás _______________ {estilo_la} ')
            if estilo_la == 'Raspado':
                print(f'Raspado lados/trás ______________ {raspado} ')
            else:
                print(f'Raspado lados/trás ______________ --- ')
            print(
                f'Cor do cabelo editado ___________ R:{cor_cabelo_R} / G:{cor_cabelo_G} / B:{cor_cabelo_B} ')
            print(f'Acessórios ______________________ {acessorio} ')
            if acessorio == 'Ligado':
                print(f'Cor do acessório ________________ {cor_acessorio} ')
            else:
                print(f'Cor do acessório ________________ --- ')

        else:
            pass


imprimir_cabelo()
print()
