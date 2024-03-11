from fnmatch import translate
from multiprocessing import Value
from textwrap import fill
from tkinter import CENTER
import customtkinter as ctkn
from deep_translator import GoogleTranslator
from requests import options


ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')

def traducao():



root = ctkn.CTk()
root.minsize(900,700)
root.maxsize(1000,700)
root.title('Tradutor Universal V1.0')
ctkn.CTkLabel(root,text='Tradutor Universal V1.0', font=('Arial', 25,'bold'), text_color='white').pack(anchor=ctkn.CENTER,pady=5)
caixa = ctkn.CTkFrame(root, width =700, height=800,fg_color='transparent')
caixa.pack(fill=ctkn.X, padx=20, pady=10)

ctkn.CTkLabel(caixa,text='Texto Para Traduzir👌:', font=('Arial', 18,'bold'), text_color='white').pack(fill=ctkn.X )

texto = ctkn.CTkEntry(caixa,placeholder_text='Insira o texto que deseja traduzir',width=100, height=200, bg_color='white')
texto.pack(fill=ctkn.X)

traduzir = GoogleTranslator().get_supported_languages()
entrada_i = ctkn.StringVar(value='english')
saida_i = ctkn.StringVar(value='english')

idioma_e = ctkn.CTkOptionMenu(caixa,width=50, height=30,  values= traduzir, variable = entrada_i )
idioma_e.pack(pady=5)
idioma_e.set('portuguese')

idioma_s = ctkn.CTkOptionMenu(caixa,width=50, height=30, values= traduzir, variable = saida_i)
idioma_s.pack(pady=5)
idioma_s.set('english')

botao = ctkn.CTkButton(caixa, text='Traduzir', font=('Arial', 18,'bold'), text_color='white')
botao.pack(fill=ctkn.X,pady=10)

ctkn.CTkLabel(caixa,text='Texto Traduzido:', font=('Arial', 18,'bold'), text_color='white').pack(fill=ctkn.X )
texto_traduzido = ctkn.CTkEntry(caixa,placeholder_text='Tradução',width=100, height=200, bg_color='white')
texto_traduzido.pack(fill=ctkn.X)






root.mainloop() 