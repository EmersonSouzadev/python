# import tkinter




# janela = tkinter.Tk()

# janela.geometry('500x300')
# janela.title('Janela 1')
# def clique():
#    print("Você Clicou")

# titulo = tkinter.Label(janela,text='Bem vindo ao Ao APP')
# titulo.pack(padx=10,pady=10)

# botao = tkinter.Button(janela, text='Clique aqui', command= clique)
# botao.pack(padx=15,pady=15)

# janela.mainloop()
# ----------------
import customtkinter as ttk


ttk.set_appearance_mode('dark')
janela = ttk.CTk()

janela.geometry('500x300')

titulo = ttk.CTkLabel(janela,text='Bem vindo Ao App', text_color='white',font=('sans-serif', 20))
titulo.pack(padx= 10, pady=10)
h1login = ttk.CTkLabel(janela,text='Login', text_color='white',font=('sans-serif', 15))
h1login.pack(padx= 5, pady= 5)

login = ttk.CTkEntry(janela, placeholder_text='Digite seu Login',width=200)
login.pack(padx= 5, pady=5)
# h1senha = ttk.CTkLabel(janela,text='Senha', text_color='white',font=('sans-serif', 15))
# h1senha.pack(padx= 1, pady= 1)
senha = ttk.CTkEntry(janela, placeholder_text='Digite sua senha',width=200, show='*')
senha.pack(padx= 5, pady=5)

 
botao = ttk.CTkButton(janela, text='Entrar')
botao.pack(padx= 10, pady=10)



janela.mainloop()