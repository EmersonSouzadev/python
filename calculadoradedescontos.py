from struct import pack
import customtkinter as c

c.set_appearance_mode('light')
c.set_default_color_theme('blue')
janela = c.CTk()
janela.minsize(450,400)
janela.maxsize(600,500)
janela.title('Aplicador de descontos :')
c.CTkLabel(janela,text='Aplicador de descontos:', font=('Arial', 20,'bold'), text_color='black').pack(anchor=c.CENTER,pady=5)
caixa = c.CTkFrame(janela, width =700, height=800,fg_color='transparent')
caixa.pack(fill=c.X, padx=20, pady=10)

def calcular():
 
 p = float(preco.get())
 d = float(desconto.get())
 
 valor_desconto = (d/100) * p
 
 valor_final =  p - valor_desconto

 
 
 
 resultado.configure(text= f'O valor com Desconto é  R$:{valor_final:.2f} !')
 





c.CTkLabel(caixa,text='Valor do Produto R$:', font=('Arial', 15,'italic'), text_color='black').pack(fill=c.X )

preco = c.CTkEntry(caixa,placeholder_text='Insira o Valor do produto R$:',width=200, height=30, bg_color='black')

preco.pack(pady=10,padx=10)

c.CTkLabel(caixa,text='Desconto aplicado no Produto:', font=('Arial', 15,'italic'), text_color='black').pack(fill=c.X )

desconto = c.CTkEntry(caixa,placeholder_text='Insira o Desconto %:',width=200, height=30, bg_color='black')
desconto.pack(pady=10,padx=10)
botao = c.CTkButton(caixa, text='APLICAR DESCONTO', font=('Arial', 12,'bold'), text_color='black', command=calcular)
botao.pack(pady=10,padx=10)

resultado = c.CTkLabel(caixa, text='', text_color='darkblue', font =('verdana',20 , 'bold'))
resultado.pack(padx=10, pady=10) #posição resultado







janela.mainloop()