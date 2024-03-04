
import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')

root = ctkn.CTk()

root.title('Combustivel APP 2024')

root.geometry('500x500')


def calculo():
 d = int(distancia.get())
 c = int(consumo.get())
 v = float(valor.get())
     
 preco = (d/c) * v
 
 
 resultado.configure(text= f'O Gasto total da Viagem foi R$ {preco:.2f} ')
 
 
     
         
#  --------------
root.iconbitmap('petrol_can_icon_227553.ico')

titulo = ctkn.CTkLabel(root , text='App Calcular Consumo em Viagem',text_color='white',font= ('Verdana', 15, 'bold'))
titulo.pack(padx= 10, pady=10)

distancia = ctkn.CTkEntry(root,placeholder_text='Digite a distância da Viagem', width=220,height=30, fg_color='White',text_color='black')
distancia.pack(padx= 10, pady=10)

consumo= ctkn.CTkEntry(root, placeholder_text='Digite o consumo (KM/H)', width=220,height=30, fg_color='White', text_color='black')
consumo.pack(padx= 10, pady=10)


valor = ctkn.CTkEntry(root,placeholder_text='Digite a valor por litro', width=220,height=30, fg_color='White',text_color='black')
valor.pack(padx= 10, pady=10)

calcular = ctkn.CTkButton(root, text='Calcular', width=150 , height=34, command= calculo) #Botão
calcular.pack(padx= 10, pady=10) #posição botão

resultado = ctkn.CTkLabel(root, text='', text_color='darkgreen', font =('verdana',20 , 'bold'))
resultado.pack(padx=10, pady=10) #posição resultado




root.mainloop( )
# rodar janela
                                
#final ------------