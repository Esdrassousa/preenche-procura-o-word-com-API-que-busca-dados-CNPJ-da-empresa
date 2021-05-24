import json

import tkinter as tk
from tkinter import *

from Classes_funcoes_Procuracao_pessoa_Fisica import *

from Classes_funcoes_Procuracao_pessoa_Juridica import *




def janela_pessoa_fisica():
    
    a = CPF()

def janela_pessoa_juridica():
    b = CNPJ()


janela_main = tk.Tk()




bt_cpf = Button(janela_main , width = 20 , text="Pessoa Física" , command = janela_pessoa_fisica)
bt_cpf.place(x=12,y=100)

bt_cnpj = Button(janela_main,width =20 , text="Pessoa Juridica", command=janela_pessoa_juridica)
bt_cnpj.place(x=12, y=150)

janela_main.geometry("300x300+200+200")
janela_main.title("Procuração")
janela_main.mainloop()
