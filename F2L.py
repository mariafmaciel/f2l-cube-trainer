#CFOP.py
#F2L treiner

import os
os.system('cls')
import random
my_dic_emb = {"1" : "U F R' F D' F' D R F' U'",
                "2" : "R B U' B' U' R' U",
                "3" : "L' B2 D2 R2 B2 L2 U2 R2 F2 L' R' U' R y",
                "4" : "B' L' D' L2 D' U B2 D B2 D U' L' B R U' R'",
                "5" : "L2 D2 U2 L2 R2 D2 U2 R' U2 R U' R' U",
                "6" : "L2 D2 U2 L2 R2 D2 U2 R' U' R' U F' U F U'",
                "7" : "L2 D2 U2 L2 R2 D2 U2 R' U2 R U2 R' U",
                "8" : "D2 L2 R2 D2 U2 L2 R2 U2 R' U' R U2 R U'",
                "9" : "R2 U R2 U R2 U' R2 U' R' U2 R F R2 F' y",
                "10" : "L2 D2 U2 L2 R2 D2 U2 R' U' R' U' R U' R' U",
                "11" : "R2 U R2 U2 R2 U' R U R U F R2 F' U y",
                "12" : "U' R2 U2 F2 L2 D B2 D' L2 F2 R2 U2 R' U2 R' U'",
                "13" : "B2 U2 B2 F2 D B2 L2 B2 D R D2 R' D2 F2 U' R y",
                "14" : "B2 R2 U2 B2 U F2 R2 F2 U R' F2 R' B2 F2 U' R'",
                "15" : "F2 U2 F2 D' U' U' B2 D L' F2 L D2 R2 U R2 B2 D2",
                "16" : "D2 L2 R2 D2 U2 L2 R2 U2 R' U F' U F U2 R y",
                #simple scramble
                "16" : "F' U F U2 R U R'",
                "17" : "R U' R' U R U2 R'",
                "18" : "R U R' U' R U R' F R' F' R",
                "19" : "R U R' U' R U2 R' U'",
                "20" : "R U R' F R' F' R2 U R' U",
                "21" : "R B U2 B' R'",
                "22" : "F' L' U2 L F",
                "23" : "R U' R' U R U' R' U2 R U' R'",
                "24" : "R U R' F R U R' U' F'",
                "25" : "F' R U R' U' R' F R",
                "26" : "F' U' F U R U R' U'",
                "27" : "R U R' U' R U R'",
                "28" : "R' F R F' U R U' R'",
                "29" : "F R' F' R F R' F' R",
                "30" : "R U' R' U R U' R'",
                "31" : "R U R' F R' F' R U",
                "32" : "R U' R' U R U' R' U R U' R'",
                "33" : "R U R' U2 R U R' U",
                "34" : "R U' R' U2 R U' R' U'",
                "35" : "F' U F U' R U' R' U",
                "36" : "R U' R' U2 F R' F' R U2",
                "37" : "R U' R U2 F R2 F' U2 R2",
                "38" : "R U' R' U R U2 R' U R U' R'",
                "39" : "R U' R' U' R U R' U2 R U' R'",
                "40" : "R U R' F U R U' R' F' R U R'",
                "41" : "R F U R U' R' F' U' R'"}
my_dic_sol = {'1' : "U R U' R'",
              '2' : "R R' F' R",
              '3' : "F' U' F",
              '4' : "R U' R'",
              '5' : "U' R U R' U2 R U' R'",
              '6' : "U' Rw U' R' U R U Rw",
              '7' : "U' R U2 R' U' R U2 R'",
              '8' : "Dw R U2 R U R' U2 R",
              '9' : "U' R U' R' U F' U' F",
             '10' : "U'' R U R' U R U R' ",
             '11' : "Y' R U2 R2 U' R'",
             '12' : "R U' R' U R U' R' U2 R U' R'",
             '13' : "y' U R' U R U' R' U' R",
             '14' : "U' R U' R' U R U R'",
             '15' : "R U R' U2 R U' R' U R U' R'",
             '16' : "R U' R' U2 F' U' F",
             '17' : "R U2 R' U' R U R'",
             '18' : "y' R' U2 R U R' U' R",      
             '19' : "U R U2 R' U R U' R'",
             '20' : "Y' U' R' U2 R U' R' U R",
             '21' : "U2 R U R' U R U' R'",
             '22' : "Rw U' Rw' U2 Rw U RW'",
             '23' : "U R U' R' U' R U' R' U R U' R'",
             '24' : "y' R' U' R U2 R' U' R U R' U' R",
             '25' : "U' R' F R F' R U R'",
             '26' : "U R U' R' F R' F' R",
             '27' : "R U' R' U R U' R'",
             '28' : "R U R' U' F R' F' R",
             '29' : "R' F R F' R' F R F'",
             '30' : "F R' F' R F R' F' R",
             '31' : "R U' R' F' U2 F",
             '32' : "U R U' R' U R U' R' U R U' R'",
             '33' : "U' R U' R' U2 R U' R'",
             '34' : "U R U R' U2 R U R'",
             '35' : "U' R U R' U F' U' F",
             '36' : "U F' U' F U' R U R'",
             '37' : "R2 U2 F R2 F' U2 R' U R'",
             '38' : "R U' R' U' R U R' U2 R U' R'",
             '39' : "R U' R' U R U2 R' U R U' R'",
             '40' : "F' L' U2 L F R U R'",
             '41' : "R U' R' F' L' L' U2 L F"}
while True:
 resposta = input("Olá, vamos treinar F2L? Sim ou Não?\n")
 if resposta == "sim":
     resposta1 = input('Voce quer visualizar o embaralhamento, a solução ou os dois?\n')
     if resposta1 == 'solucao':
        number1 = input('Qual caso de F2L você tem em mente?\n')
        print (f'Aqui esta a solução n°{number1}:\n')
        print (f'\n-----{my_dic_sol[(number1)]}-----\n')
     elif resposta1 == 'embaralhamento':
       TDE = input ('Quer testar um embaralhamento aleatorio ou especifico?\n ')
       if TDE == 'aleatorio':
          #transformando dic. em lista
          consult_dic = list(my_dic_emb.keys())
          n_do_caso = random.choice(consult_dic)
          print (f'Aqui esta o embaralhamento do caso n° {n_do_caso}:\n')
          print (f'\n-----{my_dic_emb[(n_do_caso)]}-----\n')
       elif TDE == 'especifico':
        number2 = input("Qual caso de F2L você tem em mente?\n")
        print (f"Aqui esta o embaralhamento do caso n°{number2}:\n")
        print (f'\n-----{my_dic_emb[(number2)]}-----\n')
     elif resposta1 == 'os dois':
        TPD = input ('Quer testar algoritmos especificos ou aleatorios?\n')
        if TPD == 'especificos':
         number3 = input("Qual caso de F2L você tem em mente?\n")
         print (f"Aqui esta a solução e embaralhamento do caso n°{number3}:\n")
         print ('Embaralhamento:\n')
         print (f'-----{my_dic_sol[(number3)]}-----\n')
         print ('Solução:\n')
         print (f'-----{my_dic_emb[(number3)]}-----\n')
        elif TPD == 'aleatorios':
          consult_dic = list(my_dic_sol.keys())
          n_do_caso = random.choice(consult_dic)
          print (f'Aqui esta o embaralhamento do caso n° {n_do_caso}:\n')
          print (f'-----{my_dic_emb[(n_do_caso)]}-----\n')
          print (f'Aqui esta a solução do caso n° {n_do_caso}:\n')
          print (f'-----{my_dic_sol[(n_do_caso)]}-----\n')
 elif resposta == 'nao':
   sair = input ('Deseja sair do programa?\n')
   if sair == 'sim':
      break
   elif sair == 'nao':
      print ( 'Vamos tentar denovo!\n')
            