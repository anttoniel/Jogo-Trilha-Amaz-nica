import sqlite3

import random

import pygame

from pygame.locals import *

from sys import exit
 
pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
  pygame.display.update()
#ARMAZENANDO DADOS DE CADASTRO EM UM BANCO DE DADOS



#CADASTRO DO PLAYER 1

print("  BEM VINDO(A) AO JOGO DA TRILHA AMAZÔNICA!  ")

nome = input("  PLAYER1, INSIRA SEU NOME:   ")

cadastrado1= input("   DESEJA BUSCAR UM CADASTRO FEITO ANTERIORMENTE? [s/n]  ")
con = sqlite3.connect('dados_cadastro.db')

cursor = con.cursor()
if cadastrado1 == "s":
   cursor.execute(f"SELECT nome FROM NOME")
   for row in cursor.fetchone():
    print("  ",row)
print("  \n PLAYER1, CADASTRE-SE PARA JOGAR:   ")

nome = input("  NOME:   ")

idade = int(input("  IDADE:  "))

while idade < 6:

   print("  VOCÊ NÃO POSSUI IDADE SUFICIENTE PARA JOGAR!  ")

   idade = int(input("  IDADE:  "))

else:

  print(f"{nome}, seja bem vindo(a)!")

 

email = input("  EMAIL:   ")

while email.find("@") == -1:

  print("  INSIRA UM EMAIL VÁLIDO! ")

  email = input("  EMAIL:   ")

else:

  print("  EMAIL VÁLIDO!  ")


 

#CADASTRO DO PLAYER2

print("  \n PLAYER2, CADASTRE-SE PARA JOGAR:   ")

nome2 = input("  NOME:   ")

idade2 = int(input("  IDADE:  "))

while idade2 < 6:

   print("  VOCÊ NÃO POSSUI IDADE SUFICIENTE PARA JOGAR!  ")

   idade2 = int(input("  IDADE:  "))

else:

  print(f"{nome2}, seja bem vindo(a)!")

 

email2 = input("  EMAIL:   ")

while email2.find("@") == -1:

  print("  INSIRA UM EMAIL VÁLIDO! ")

  email2 = input("  EMAIL:   ")

else:

  print("  EMAIL VÁLIDO!  ")

print("\n  CADASTROS FINALIZADOS!  ")

dado = [1,2,3,4,5,6]

tutorial = input("\n  DESEJA INICIAR O TUTORIAL? [s/n]  ")

dadoteste1 = random.choice(dado)
dadoteste2 = random.choice(dado)

if tutorial == "s":
  print("\n  O JOGO CONSISTE EM UMA CORRIDA ALTERNADA POR 2 PLAYERS EM 4 RODADAS, A CADA RODADA O PLAYER PRECISA JOGAR OS DOIS DADOS PARA SABER QUANTAS CASAS DEVERÁ ANDAR PELA SOMA DE SEUS VALORES, APÓS AS 4 RODADAS, O TRILHEIRO QUE PERCORREU MAIS CASAS VENCE. ")
  
  print("\n------------ RODADA TESTE ------------")
  rodadatest = input("  INSIRA 'd' PARA JOGAR OS DADOS:  ")
  while rodadatest != "d":
   print("\n  VOCÊ NÃO JOGOU OS DADOS, DIGITOU A TECLA ERRADA!  ")
   rodadatest = input(" INSIRA 'd' PARA JOGAR OS DADOS:  ")
    
  if rodadatest == "d":
    print(f"\n  MUITO BEM! OS VALORES DOS DADOS FORAM {dadoteste1} E {dadoteste2}  ")
 

start = input("  PRESSIONE ENTER PARA INICIAR O JOGO  ")


dado1 = random.choice(dado)
dado2 = random.choice(dado)
dado3 = random.choice(dado)
dado4 = random.choice(dado)
dado5 = random.choice(dado)
dado6 = random.choice(dado)
dado7 = random.choice(dado)
dado8 = random.choice(dado)
dado9 = random.choice(dado)
dado10= random.choice(dado)
dado11= random.choice(dado)
dado12 = random.choice(dado)
dado13 = random.choice(dado)
dado14 = random.choice(dado)
dado15 = random.choice(dado)
dado16 = random.choice(dado)



print("\n-----------------RODADA 1-----------------")
d = input(f"{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado1} E {dado2}!  " )
        c11 = dado1 + dado2
        if dado1 == dado2:
                c11 = c11*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p11 = c11
        if 8>p11<13:
                print("VOCÊ ENCONTROU UMA NOVA ESPÉCIE RARA DE RÃS EM SUA TRILHA, AVANCE MAIS DUAS CASAS!")
                c11 = c11 + 2
                p11 = c11 
        print(f"PLAYER1 AVANÇA {c11} CASAS E FICA NA CASA {p11}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        p11 = c11 = 0

d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado3} E {dado4}!  " )
        c21 = dado3 + dado4
        if dado3 == dado4:
                c21 = c21*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p21 = c21
        if 8>p21<13:
                print("VOCÊ ENCONTROU UMA NOVA ESPÉCIE RARA DE RÃS EM SUA TRILHA, AVANCE MAIS DUAS CASAS!")
                c21 = c21 + 2
                p21 = c21
        print(f"PLAYER2 AVANÇA {c21} CASAS E FICA NA CASA {p21}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        p21 = c21 = 0

print("\n-----------------RODADA 2-----------------")
d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado5} E {dado6}!  " )
        c12 = dado5 + dado6
        if dado5 == dado6:
                c12 = c12*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p12 = c12 + p11
        if 18>p12<23:
          print("VOCÊ FOI ATACADO POR UMA CASCAVEL NO CAMINHO E NÃO PÔDE AVANÇAR 3 CASAS! ")
          c12 = c12 - 3
          p12 = p12 - 3
        
         
        print(f"PLAYER1 AVANÇA {c12} CASAS E FICA NA CASA {p12}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c12 = 0
        p12 = c12 + p11 


d = input(f"\n{nome2} DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado7} E {dado8}!  " )
        c22 = dado7 + dado8
        if dado7 == dado8:
                c22 = c22*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p22 = c22 + p21
        if 18>p22<23:
          print("VOCÊ FOI ATACADO POR UMA CASCAVEL NO CAMINHO E NÃO PÔDE AVANÇAR 3 CASAS! ")
          c22 = c22 - 3
          p22 = p22 - 3
        print(f"PLAYER2 AVANÇA {c22} CASAS E FICA NA CASA {p22}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c22 = 0
        p22 = c22 + p21

print("\n-----------------RODADA 3-----------------")
d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado9} E {dado10}!  " )
        c13 = dado9 + dado10
        if dado9 == dado10:
                c13 = c13*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p13 = c13 + p12
        print(f"PLAYER1 AVANÇA {c13} CASAS E FICA NA CASA {p13}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c13 = 0
        p13 = c13 + p12

d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado11} E {dado12}!  " )
        c23 = dado11 + dado12
        if dado11 == dado12:
                c23 = c23*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p23 = c23 + p22
        print(f"PLAYER2 AVANÇA {c23} CASAS E FICA NA CASA {p23}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c23 = 0
        p23 = c23 + p22

print("\n-----------------RODADA 4-----------------")
d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado13} E {dado14}!  " )
        c14 = dado13 + dado14
        if dado13 == dado14:
                c13 = c14*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p14 = c14 + p13
        print(f"PLAYER1 AVANÇA {c14} CASAS E FICA NA CASA {p14}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c14 = 0
        p14 = c14 + p13

d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
if d == "d":
        print(f"\n    OS VALORES DOS DADOS FORAM {dado15} E {dado16}!  " )
        c24 = dado15 + dado16
        if dado15 == dado16:
                c24 = c24*2
                print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
        p24 = c24 + p23
        print(f"PLAYER2 AVANÇA {c24} CASAS E FICA NA CASA {p24}.")
        
else: 
        print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
        c24 = 0
        p24 = c24 + p23

if p14 > p24:
        print(f"\n {nome} VENCEU O JOGO !!! {p14-p24} CASAS À FRENTE DE {nome2} NA TRILHA.   ")
elif p14 == p24:
        print(f"\n        HOUVE UM EMPATE! {nome} e {nome2} TERMINARAM A TRILHA NA MESMA CASA.    ")
elif p24 > p14:
        print(f"\n {nome2} VENCEU O JOGO !!! {p24-p14} CASAS À FRENTE DE {nome} NA TRILHA.   ") 
#ARMAZENAMENTO DO CADASTRO DO PLAYER 1 NO BANCO DE DADOS
cursor.execute(f"INSERT INTO PLAYERS VALUES('{nome}','{idade}','{email}','{p14}')")

con.commit()
#ARMAZENAMENTO DO CADASTRO DO PLAYER 2 NO BANCO DE DADOS
cursor.execute(f"INSERT INTO PLAYERS VALUES('{nome2}','{idade2}','{email2}','{p24}')")

con.commit()

restart = input("\n INSIRA 'j' PARA JOGAR DE NOVO OU ENTER PARA ENCERRAR:  ")

while restart == "j":


 print("\n  BEM VINDO(A) AO JOGO DA TRILHA AMAZÔNICA!  ")
 novocadastro = input("\n DESEJA CADASTRAR NOVOS PLAYERS? [s/n] ")
 if novocadastro == 's':
  print("  \n PLAYER1, CADASTRE-SE PARA JOGAR:   ")

  nome = input("  NOME:   ")

  idade = int(input("  IDADE:  "))

  while idade < 6:

     print("  VOCÊ NÃO POSSUI IDADE SUFICIENTE PARA JOGAR!  ")

     idade = int(input("  IDADE:  "))

  else:

    print(f"{nome}, seja bem vindo(a)!")

 

  email = input("  EMAIL:   ")

  while email.find("@") == -1:

    print("  INSIRA UM EMAIL VÁLIDO! ")

    email = input("  EMAIL:   ")

  else:

   print("  EMAIL VÁLIDO!  ")

 

 

  

 #CADASTRO DO PLAYER2

  print("  \n PLAYER2, CADASTRE-SE PARA JOGAR:   ")

  nome2 = input("  NOME:   ")

  idade2 = int(input("  IDADE:  "))

  while idade2 < 6:

     print("  VOCÊ NÃO POSSUI IDADE SUFICIENTE PARA JOGAR!  ")

     idade2 = int(input("  IDADE:  "))

  else:

    print(f"{nome2}, seja bem vindo(a)!")

 

  email2 = input("  EMAIL:   ")

  while email2.find("@") == -1:

    print("  INSIRA UM EMAIL VÁLIDO! ")

    email2 = input("  EMAIL:   ")

  else:

    print("  EMAIL VÁLIDO!  ")

 




  print("\n  CADASTROS FINALIZADOS!  ")

 if novocadastro == 'n':
  print("  PLAYERS MANTIDOS! ")
 dado = [1,2,3,4,5,6]

 

 start = input("  PRESSIONE ENTER PARA INICIAR O JOGO  ")


 dado1 = random.choice(dado)
 dado2 = random.choice(dado)
 dado3 = random.choice(dado)
 dado4 = random.choice(dado)
 dado5 = random.choice(dado)
 dado6 = random.choice(dado)
 dado7 = random.choice(dado)
 dado8 = random.choice(dado)
 dado9 = random.choice(dado)
 dado10= random.choice(dado)
 dado11= random.choice(dado)
 dado12 = random.choice(dado)
 dado13 = random.choice(dado)
 dado14 = random.choice(dado)
 dado15 = random.choice(dado)
 dado16 = random.choice(dado)



 print("\n-----------------RODADA 1-----------------")
 d = input(f"{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado1} E {dado2}!  " )
         c11 = dado1 + dado2
         if dado1 == dado2:
                 c11 = c11*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p11 = c11
         if 8>p11<13:
                 print("VOCÊ ENCONTROU UMA NOVA ESPÉCIE RARA DE RÃS EM SUA TRILHA, AVANCE MAIS DUAS CASAS!")
                 c11 = c11 + 2
                 p11 = c11 
         print(f"PLAYER1 AVANÇA {c11} CASAS E FICA NA CASA {p11}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         p11 = c11 = 0

 d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado3} E {dado4}!  " )
         c21 = dado3 + dado4
         if dado3 == dado4:
                 c21 = c21*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p21 = c21
         if 8>p21<13:
                 print("VOCÊ ENCONTROU UMA NOVA ESPÉCIE RARA DE RÃS EM SUA TRILHA, AVANCE MAIS DUAS CASAS!")
                 c21 = c21 + 2
                 p21 = c21
         print(f"PLAYER2 AVANÇA {c21} CASAS E FICA NA CASA {p21}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         p21 = c21 = 0

 print("\n-----------------RODADA 2-----------------")
 d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado5} E {dado6}!  " )
         c12 = dado5 + dado6
         if dado5 == dado6:
                 c12 = c12*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p12 = c12 + p11
         if 18>p12<23:
           print("VOCÊ FOI ATACADO POR UMA CASCAVEL NO CAMINHO E NÃO PÔDE AVANÇAR 3 CASAS! ")
           c12 = c12 - 3
           p12 = p12 - 3
        
         
         print(f"PLAYER1 AVANÇA {c12} CASAS E FICA NA CASA {p12}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c12 = 0
         p12 = c12 + p11 


 d = input(f"\n{nome2} DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado7} E {dado8}!  " )
         c22 = dado7 + dado8
         if dado7 == dado8:
                 c22 = c22*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p22 = c22 + p21
         if 18>p22<23:
           print("VOCÊ FOI ATACADO POR UMA CASCAVEL NO CAMINHO E NÃO PÔDE AVANÇAR 3 CASAS! ")
           c22 = c22 - 3
           p22 = p22 - 3
         print(f"PLAYER2 AVANÇA {c22} CASAS E FICA NA CASA {p22}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c22 = 0
         p22 = c22 + p21

 print("\n-----------------RODADA 3-----------------")
 d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado9} E {dado10}!  " )
         c13 = dado9 + dado10
         if dado9 == dado10:
                 c13 = c13*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p13 = c13 + p12
         print(f"PLAYER1 AVANÇA {c13} CASAS E FICA NA CASA {p13}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c13 = 0
         p13 = c13 + p12

 d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado11} E {dado12}!  " )
         c23 = dado11 + dado12
         if dado11 == dado12:
                 c23 = c23*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p23 = c23 + p22
         print(f"PLAYER2 AVANÇA {c23} CASAS E FICA NA CASA {p23}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c23 = 0
         p23 = c23 + p22

 print("\n-----------------RODADA 4-----------------")
 d = input(f"\n{nome}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado13} E {dado14}!  " )
         c14 = dado13 + dado14
         if dado13 == dado14:
                 c13 = c14*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p14 = c14 + p13
         print(f"PLAYER1 AVANÇA {c14} CASAS E FICA NA CASA {p14}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c14 = 0
         p14 = c14 + p13

 d = input(f"\n{nome2}, DIGITE 'd' PARA JOGAR OS DADOS ")
 if d == "d":
         print(f"\n    OS VALORES DOS DADOS FORAM {dado15} E {dado16}!  " )
         c24 = dado15 + dado16
         if dado15 == dado16:
                 c24 = c24*2
                 print("VOCÊ ESTÁ COM SORTE! CONSEGUIU NÚMEROS IGUAIS NOS DADOS E VAI AVANÇAR O DOBRO DE CASAS!")
         p24 = c24 + p23
         print(f"PLAYER2 AVANÇA {c24} CASAS E FICA NA CASA {p24}.")
        
 else: 
         print(" VOCÊ NÃO JOGOU OS DADOS E PASSOU A VEZ! ")
         c24 = 0
         p24 = c24 + p23

 if p14 > p24:
         print(f"\n {nome} VENCEU O JOGO !!! {p14-p24} CASAS À FRENTE DE {nome2} NA TRILHA.   ")
 elif p14 == p24:
         print(f"\n        HOUVE UM EMPATE! {nome} e {nome2} TERMINARAM A TRILHA NA MESMA CASA.    ")
 elif p24 > p14:
         print(f"\n {nome2} VENCEU O JOGO !!! {p24-p14} CASAS À FRENTE DE {nome} NA TRILHA.   ") 

 cursor.execute(f"INSERT INTO PLAYERS VALUES('{nome}','{idade}','{email}','{p14}')")

 con.commit()
 #ARMAZENAMENTO DO CADASTRO DO PLAYER 2 NO BANCO DE DADOS
 cursor.execute(f"INSERT INTO PLAYERS VALUES('{nome2}','{idade2}','{email2}','{p24}')") 
 con.commit()

 restart = input(" INSIRA 'j' PARA JOGAR DE NOVO OU 'Enter' PARA ENCERRAR:  ")
else:
 print("\n VOLTE SEMPRE À TRILHA AMAZÔNICA !!!  ")  
 cursor.execute(f"SELECT SCORE, NOME FROM PLAYERS ORDER BY SCORE DESC")
 print("\n  --- RANKING FINAL ---   \n PONTOS/PLAYERS: ")
 for row in cursor.fetchall():
   print("  ",row)
 
 
 

  
  

