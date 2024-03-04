import os
import random

numeroaleatorio = random.randint(1,100)
while True:
 palpite = int(input('Digite um numero de 1 a 100 :'))
 os.system('cls')

 if  palpite == numeroaleatorio:
  print('Você a certou o numero é :', palpite ,'!')
  break

 elif palpite < numeroaleatorio:
   print(palpite,'é Muito Baixo, Tento Novamente !')


 elif palpite > numeroaleatorio:
    print(palpite,' é muito Alto, Tente Novamente!')   
    
    
     


