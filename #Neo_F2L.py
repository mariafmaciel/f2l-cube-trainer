# Neo_F2L

import sys
import time
import random
import os
os.system('cls')
# Dicionário de embaralhamentos e soluções
my_dic_emb = {"1": "U F R' F D' F' D R F' U'",
              "2": "R B U' B' U' R' U",
              "3": "L' B2 D2 R2 B2 L2 U2 R2 F2 L' R' U' R y",
              "4": "B' L' D' L2 D' U B2 D B2 D U' L' B R U' R'",
              "5": "L2 D2 U2 L2 R2 D2 U2 R' U2 R U' R' U",
              "6": "L2 D2 U2 L2 R2 D2 U2 R' U' R' U F' U F U'",
              "7": "L2 D2 U2 L2 R2 D2 U2 R' U2 R U2 R' U",
              "8": "D2 L2 R2 D2 U2 L2 R2 U2 R' U' R U2 R U'",
              "9": "R2 U R2 U R2 U' R2 U' R' U2 R F R2 F' y",
              "10": "L2 D2 U2 L2 R2 D2 U2 R' U' R' U' R U' R' U",
              "11": "R2 U R2 U2 R2 U' R U R U F R2 F' U y",
              "12": "U' R2 U2 F2 L2 D B2 D' L2 F2 R2 U2 R' U2 R' U'",
              "13": "B2 U2 B2 F2 D B2 L2 B2 D R D2 R' D2 F2 U' R y",
              "14": "B2 R2 U2 B2 U F2 R2 F2 U R' F2 R' B2 F2 U' R'",
              "15": "F2 U2 F2 D' U' U' B2 D L' F2 L D2 R2 U R2 B2 D2",
              "16": "D2 L2 R2 D2 U2 L2 R2 U2 R' U F' U F U2 R y",
              # simple scramble
              "16": "F' U F U2 R U R'",
              "17": "R U' R' U R U2 R'",
              "18": "R U R' U' R U R' F R' F' R",
              "19": "R U R' U' R U2 R' U'",
              "20": "R U R' F R' F' R2 U R' U",
              "21": "R B U2 B' R'",
              "22": "F' L' U2 L F",
              "23": "R U' R' U R U' R' U2 R U' R'",
              "24": "R U R' F R U R' U' F'",
              "25": "F' R U R' U' R' F R",
              "26": "F' U' F U R U R' U'",
              "27": "R U R' U' R U R'",
              "28": "R' F R F' U R U' R'",
              "29": "F R' F' R F R' F' R",
              "30": "R U' R' U R U' R'",
              "31": "R U R' F R' F' R U",
              "32": "R U' R' U R U' R' U R U' R'",
              "33": "R U R' U2 R U R' U",
              "34": "R U' R' U2 R U' R' U'",
              "35": "F' U F U' R U' R' U",
              "36": "R U' R' U2 F R' F' R U2",
              "37": "R U' R U2 F R2 F' U2 R2",
              "38": "R U' R' U R U2 R' U R U' R'",
              "39": "R U' R' U' R U R' U2 R U' R'",
              "40": "R U R' F U R U' R' F' R U R'",
              "41": "R F U R U' R' F' U' R'"}
my_dic_sol = {'1': "U R U' R'",
              '2': "R R' F' R",
              '3': "F' U' F",
              '4': "R U' R'",
              '5': "U' R U R' U2 R U' R'",
              '6': "U' Rw U' R' U R U Rw",
              '7': "U' R U2 R' U' R U2 R'",
              '8': "Dw R U2 R U R' U2 R",
              '9': "U' R U' R' U F' U' F",
              '10': "U'' R U R' U R U R' ",
              '11': "Y' R U2 R2 U' R'",
              '12': "R U' R' U R U' R' U2 R U' R'",
              '13': "y' U R' U R U' R' U' R",
              '14': "U' R U' R' U R U R'",
              '15': "R U R' U2 R U' R' U R U' R'",
              '16': "R U' R' U2 F' U' F",
              '17': "R U2 R' U' R U R'",
              '18': "y' R' U2 R U R' U' R",
              '19': "U R U2 R' U R U' R'",
              '20': "Y' U' R' U2 R U' R' U R",
              '21': "U2 R U R' U R U' R'",
              '22': "Rw U' Rw' U2 Rw U RW'",
              '23': "U R U' R' U' R U' R' U R U' R'",
              '24': "y' R' U' R U2 R' U' R U R' U' R",
              '25': "U' R' F R F' R U R'",
              '26': "U R U' R' F R' F' R",
              '27': "R U' R' U R U' R'",
              '28': "R U R' U' F R' F' R",
              '29': "R' F R F' R' F R F'",
              '30': "F R' F' R F R' F' R",
              '31': "R U' R' F' U2 F",
              '32': "U R U' R' U R U' R' U R U' R'",
              '33': "U' R U' R' U2 R U' R'",
              '34': "U R U R' U2 R U R'",
              '35': "U' R U R' U F' U' F",
              '36': "U F' U' F U' R U R'",
              '37': "R2 U2 F R2 F' U2 R' U R'",
              '38': "R U' R' U' R U R' U2 R U' R'",
              '39': "R U' R' U R U2 R' U R U' R'",
              '40': "F' L' U2 L F R U R'",
              '41': "R U' R' F' L' L' U2 L F"}

# funções
def digitar(texto, velocidade=0.04):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

def limpar():
    os.system('cls')

# Programa
while True:
    limpar()
    digitar("---F2L Trainer- CFOP---\n")
    digitar("\n1- Abrir Programa\n")
    digitar("2- Sair do Programa\n")
    digitar("\nOpção:")
    resposta1 = input()
    limpar()
    if resposta1 == '1':
        while True:
            limpar()
            digitar("Bem-Vindo ao F2L Trainer!\n")
            digitar("O que você deseja fazer?\n")
            digitar("\n1- Treinar com embaralhamentos.\n")
            digitar("2- Visualizar soluções.\n")
            digitar("3- Treinar com embaralhamentos e soluções.\n")
            digitar("4- Conhecer mais sobre o método F2L.\n")
            digitar("5- Voltar para o menu inicial.\n")
            digitar("\nOpção:")
            resposta2 = input()
            limpar()
            if resposta2 == '1':
                while True:
                    digitar(
                        'Você deseja um embaralhamento específico ou aleatório?\n ')
                    digitar('\n1- Específico\n')
                    digitar('2- Aleatório\n')
                    digitar('3- voltar\n')
                    digitar('\nOpção:')
                    TDE = input()
                    limpar()
                    if TDE == '2':
                        # transformando dic. em lista
                        consult_list = list(my_dic_emb.keys())
                        # escolhendo um embaralhamento aleatorio
                        n_do_caso = random.choice(consult_list)
                        print(
                            f'\nAqui esta o embaralhamento do caso n° {n_do_caso}:\n')
                        print(f'\n-----{my_dic_emb[(n_do_caso)]}-----\n')
                    elif TDE == '1':
                        while True:
                            digitar(
                                'Qual embaralhamento você deseja visualizar?\n')
                            digitar('\nnúmero do caso de F2L:')
                            number2 = input()
                            limpar()
                            try:
                                embaralhamento = my_dic_emb[number2]
                                digitar(
                                    f'\nAqui esta o embaralhamento n°{number2}:\n')
                                print(f'\n-----{my_dic_emb[(number2)]}-----\n')
                                break
                            except KeyError:
                                limpar()
                                digitar(
                                    '\nEsse caso não existe! Digite um número entre 1 e 41!\n')
                    elif TDE == '3':
                        break
            elif resposta2 == '2':
                while True:
                    digitar('1- Escolher solução\n')
                    digitar('2- Voltar\n')
                    digitar('\nOpção:')
                    soluc = input()
                    if soluc == '1':
                        digitar('Qual solução você deseja visualizar?\n')
                        digitar('\nnúmero do caso de F2L:')
                        solucao1 = input()
                        try:
                            digitar(f'\nAqui esta a solução n°{solucao1}:\n')
                            print(f'\n-----{my_dic_sol[(solucao1)]}-----\n')
                        except KeyError:
                            limpar()
                            digitar(
                                '\nEsse caso não existe! Digite um número entre 1 e 41\n')
                    elif soluc == '2':
                        break
            elif resposta2 == '3':
                while True:
                    limpar()
                    digitar(
                        'Você deseja embaralhamento e solução específicos ou aleatórios?\n')
                    digitar('\n1- Específicos\n')
                    digitar('2- Aleatórios\n')
                    digitar('3- Voltar\n')
                    digitar('\nOpção:')
                    TPD = input()
                    if TPD == '1':
                       while True:
                        digitar(
                            'Qual embaralhamento e solução você deseja visualizar?\n')
                        digitar('\nnúmero do caso de F2L:')
                        number3 = input()
                        try:
                         digitar(
                            f"\nAqui esta a solução e embaralhamento do caso n°{number3}:\n")
                         digitar('\nEmbaralhamento:\n')
                         print(f'-----{my_dic_sol[(number3)]}-----\n')
                         digitar('Solução:\n')
                         print(f'-----{my_dic_emb[(number3)]}-----\n')
                        except KeyError:
                            limpar()
                            digitar(
                                '\nEsse caso não existe! Digite um número entre 1 e 41\n')
                    elif TPD == '2':
                        consult_dic = list(my_dic_sol.keys())
                        n_do_caso = random.choice(consult_dic)
                        digitar(
                            f'Aqui esta o embaralhamento do caso n° {n_do_caso}:\n')
                        print(f'-----{my_dic_emb[(n_do_caso)]}-----\n')
                        digitar(
                            f'Aqui esta a solução do caso n° {n_do_caso}:\n')
                        print(f'-----{my_dic_sol[(n_do_caso)]}-----\n')
                    elif TPD == '3':
                        break
            elif resposta2 == '4':
                digitar(
                    '\nO método F2L (First Two Layers) é uma das etapas do método CFOP,\n')
                digitar(
                    'utilizado para resolver o cubo magico 3x3 de forma eficiente, e em menos termpo do que o método de camadas.\n')
                digitar(
                    'O objetivo do F2L é resolver os pares de peças da primeira e segunda camada do cubo simultaneamente,\n')
                digitar(
                    'ao invés de resolver a primeira completamente antes de passar para a segunda camada.\n')
                digitar(
                    'Isso é feito identificando os pares de peças (uma peça da primeira camada e uma peça da segunda camada)\n')
                digitar(
                    'e inserindo-os na posição correta usando algoritmos específicos.\n')
                digitar('\n1- Voltar para o menu principal\n')
                digitar('2- Sair do Programa\n')
                digitar('\nOpção:')
                texto = input()
                if texto == '1':
                    break
                if texto == '2':
                    limpar()
                    sys.exit()
            elif resposta2 == '5':
                break
    elif resposta1 == '2':
        digitar('Tem certeza que deseja sair do programa?\n')
        digitar('\n1- Sim\n')
        digitar('2- Não\n')
        digitar('\nOpção:')
        sair = input()
        limpar()
        if sair == '1':
            sys.exit()
        elif sair == '2':
            continue
