
import customtkinter as ctk
import tkinter
from tkinter import *
from pytube import YouTube
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
 
janela = ctk.CTk()
janela.geometry('800x400')
janela.title('Youtube Downloader V1.1 - By Artur Brasil')
# funções ---------------------

def download():
    try:
     ytlink = link.get()
     ytobject = YouTube(ytlink, on_progress_callback= em_progresso)
     video = ytobject.streams.get_highest_resolution()
     video.download()
     texto_final.configure(text='Download Completo!')
    
    
    except:
     texto_final.configure(text='Erro no Download - Link Inválido')

def em_progresso(stream,x,bytes_restantes):
    tamanho_total = stream.filesize
    bytes_baixados = tamanho_total - bytes_restantes
    porcentagem_completa = (bytes_baixados/tamanho_total)*100
    porce = str(int(porcentagem_completa)) 
    porcento.update()
    porcento.configure(text=f'{porce}%')
   #barr de progresso
    barra.update()
    barra.set(float(porcentagem_completa/100))
         
# funções ---------------------


ctk.CTkLabel(janela, text='Youtube Downloader V1.1 Artur Brasil' , 
             font=('arial',30,'bold')).pack(pady=5)
url = tkinter.StringVar()
link = ctk.CTkEntry(janela ,placeholder_text='Digite a URL do Youtube',width=600,height=50, textvariable=url) 
link.pack(pady=20)
btn =ctk.CTkButton(janela,text='Download Video',
                   font=('arial',25,'bold'),command=download)
btn.pack(pady=5)

titulo_video = ctk.CTkLabel(janela, text='' , 
             font=('arial',18,'bold'))
titulo_video.pack(pady=5)

porcento = ctk.CTkLabel(janela,text='0%',
                         font=('arial',25,'bold'))
porcento.pack(pady=5)


barra = ctk.CTkProgressBar(janela, width=600, progress_color='red',fg_color='white')
barra.set(0)
barra.pack(pady=5)

texto_final = ctk.CTkLabel(janela, text='',
                           font=('arial',18,'bold'))
texto_final.pack(pady=5)



janela.mainloop()