import os

def principal():
   
 nomes = ['Marcio','Evelin','Vinicius','Emerson', 'Mateus','Fabio', 'Luiz','Amanda','Joao'] 
    
 print('Bem vindo ao Jogo da Adivinhação de Nomes')
 print('Tente adivinhar um nome')
 print(' Dica : os Nomes Começam com M, E , V , F, L , A ou J. ')
 while True:
  palpite = input('Digite um nome: ').strip().capitalize()
  os.system('cls')       
  if verificarnome(palpite,nomes) :
   print('Parabéns Você acertou o nome!')
   break
  
  else :  
   print(' Você errou o nome, Tente novamente!')
     

def verificarnome(palpite,nomes):
 
 if palpite in nomes: 
     return True
 else:
     return False
          
        
principal()