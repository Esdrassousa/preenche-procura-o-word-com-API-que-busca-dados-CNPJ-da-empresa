
import tkinter as tk
from tkinter import *
from tkcalendar import *
from docx import Document
import os

class CPF():
    global x_entry
    global x_lb
    x_entry = 80
    x_lb = 10
    global document
    
    print(os.path.dirname(os.path.realpath(__file__)))
    document = Document('caminho/PROCURAÇÃO.docx') 

    def inserir_entry(self,janela1,x1,y1,width1):
    
        a = tk.Entry(janela1,width=width1)
        a.place(x=x1,y=y1)
        
        return a
    
    # return a
    
    def inserir_name_label(self,janela1,x1,y1,text1):    
        
        
        Label(janela1, text=text1).place(x=x1,y=y1)
  

    def bt_inserir(self):
     for paragraph in document.paragraphs:
        nome_entry = self.tb_nome.get()
        # print(nome_entry)
        Nacionalidade_entry = self.tb_Nacionalidade.get()
        profissao_entry = self.tb_profissao.get()
        
        ###### CPF #######
        

        
        cpf_entry = self.tb_cpf.get()      
        cpf = '{}.{}.{}-{}'.format(cpf_entry[:3], cpf_entry[3:6], cpf_entry[6:9], cpf_entry[9:])
        print(cpf)
        
        ###################
        
        rg_entry = self.tb_rg.get()
        Logradouro_entry = self.tb_Logradouro.get()
        Numero_entry = self.tb_Numero.get()
        CEP_entry = self.tb_CEP.get()
        Cidade_entry = self.tb_cidade.get()
        Bairro_entry = self.tb_Bairro.get()
        paragraph.text = paragraph.text.replace("@Nome",nome_entry)
        paragraph.text = paragraph.text.replace("@NACIONALIDADE",Nacionalidade_entry)
        paragraph.text = paragraph.text.replace("@PROFISSAO",profissao_entry)
        paragraph.text = paragraph.text.replace("@CPF",cpf)
        paragraph.text = paragraph.text.replace("@RG ",rg_entry)
        paragraph.text = paragraph.text.replace("@Endereco",Logradouro_entry+" - " + Numero_entry+" - " + Bairro_entry+" - " + Cidade_entry)
        paragraph.text = paragraph.text.replace("@CEP",CEP_entry)
        
        nome_arquivos_existentes = os.listdir('C:/Users/user/OneDrive/Desktop/Projetos-Cad')
        
        path ='C:/Users/user/OneDrive/Desktop/Projetos-Cad/'+"Procuração-"+nome_entry+".docx"
        
        if path in nome_arquivos_existentes:
            os.remove(path)
            document.save('C:/Users/user/OneDrive/Desktop/Projetos-Cad/'+"Procuração-"+nome_entry+".docx")
        else:
            document.save(path)
    # def janela_pessoa_fisica():
    def __init__(self):
        janela_pessoa_fisica = tk.Tk()
        
        janela_pessoa_fisica.geometry("500x500+200+100")
        janela_pessoa_fisica.title("Procuração Pessoa Física")
        
        lb_nome = self.inserir_name_label(janela_pessoa_fisica,x_lb, 10, "Nome: ")
        
        self.tb_nome = self.inserir_entry(janela_pessoa_fisica,x_entry, 10,50)
        
        
        lb_Nacionalidade = self.inserir_name_label(janela_pessoa_fisica,x_lb, 35, "Nacionalidade")
        self.tb_Nacionalidade = self.inserir_entry(janela_pessoa_fisica,100, 35, 20)
        
        lb_profissao = self.inserir_name_label(janela_pessoa_fisica,x_lb, 60, "Profissão")
        self.tb_profissao= self.inserir_entry(janela_pessoa_fisica,x_entry, 60, 20)
        
        lb_cpf = self.inserir_name_label(janela_pessoa_fisica,x_lb, 85, "CPF")
        self.tb_cpf= self.inserir_entry(janela_pessoa_fisica,x_entry, 85, 20)
        
        lb_rg = self.inserir_name_label(janela_pessoa_fisica,x_lb, 110, "RG")
        self.tb_rg= self.inserir_entry(janela_pessoa_fisica,x_entry, 110, 20)
        
        lb_Logradouro = self.inserir_name_label(janela_pessoa_fisica,x_lb, 135, "Logradouro")
        self.tb_Logradouro= self.inserir_entry(janela_pessoa_fisica,x_entry, 135, 45)
        
        lb_Numero = self.inserir_name_label(janela_pessoa_fisica,350, 135, "Número")
        self.tb_Numero= self.inserir_entry(janela_pessoa_fisica,400, 135, 10)
        
        lb_Bairro = self.inserir_name_label(janela_pessoa_fisica,x_lb, 165, "Bairro")
        self.tb_Bairro= self.inserir_entry(janela_pessoa_fisica,x_entry, 165, 15)
        
        lb_Cidade = self.inserir_name_label(janela_pessoa_fisica,x_lb, 190,"Cidade")
        self.tb_cidade = self.inserir_entry(janela_pessoa_fisica,x_entry, 190, 20)
        
        lb_CEP = self.inserir_name_label(janela_pessoa_fisica,x_lb, 215, "CEP")
        self.tb_CEP= self.inserir_entry(janela_pessoa_fisica,x_entry, 215, 15)
        
        bt_inseir = Button(janela_pessoa_fisica, width=15, text="Inserir", command=self.bt_inserir)
        bt_inseir.place(x=10,y=290)
