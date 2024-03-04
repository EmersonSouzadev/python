
import customtkinter as ctkn
import tkinter as tk
ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')
def calculo():
 a = float(altura.get())
 p = float(peso.get())
 n = (nome.get())
 imc = p / (a * a)
 
 if imc < 16.9 :
  tipo = 'muito abaixo do peso!'
 elif imc >= 17 and imc <= 18.4 :
  tipo = 'abaixo do peso!'
 elif imc >= 18.5 and imc <= 24.9 :
  tipo = 'Peso normal!'
 elif imc >= 25 and imc <= 29.9 :
  tipo = 'Acima do Peso!'
 elif imc >= 30 and imc <= 34.9 :
  tipo = 'Obesidade grau I!'
 elif imc >= 35 and imc <= 40 :
  tipo = 'Obesidade grau II!'
 elif imc > 40:
  tipo = 'Obesidade grau III!'

 tk.messagebox(text= n + f' seu imc é :{imc:.2f} \n você está {tipo}')
 resultado.configure(text= n + f' seu imc é :{imc:.2f} \n você está {tipo}')
root = ctkn.CTk()



root.geometry('600x400')
 


root.iconbitmap('Imc.ico')
nomet = ctkn.CTkLabel(root,text='Nome :', font=('Verdana',12))
nomet.place(x=40, y=20)

nome = ctkn.CTkEntry(root,placeholder_text='Digite seu nome:', width=120,height=30, fg_color='White',text_color='black')
nome.place(x= 40, y=60)


pesot = ctkn.CTkLabel(root,text='Peso:', font=('Verdana',12))
pesot.place(x=40, y=100)

peso = ctkn.CTkEntry(root,placeholder_text='Digite seu peso :', width=120,height=30, fg_color='White',text_color='black')
peso.place(x= 40, y=140)

alturat = ctkn.CTkLabel(root,text='Altura:', font=('Verdana',12))
alturat.place(x=40, y=180)

altura= ctkn.CTkEntry(root, placeholder_text='Digite sua altura', width=120,height=30, fg_color='White', text_color='black')
altura.place(x= 40, y=220)



calcular = ctkn.CTkButton(root, text='CALCULAR IMC', width=80 , height=30, command= calculo) #Botão
calcular.place(x= 50, y=280) #posição botão

resultado = ctkn.CTkLabel(root, text='', text_color='darkgreen', font =('verdana',18, 'italic' ))
resultado.place(x=200, y=120) #posição resultado


root.mainloop()



