


import tkinter as tk
from tkinter import *
from tkcalendar import *
from docx import Document
import os
import json
import re


from Busca import *

class CNPJ():
    global x_entry
    global x_lb
    x_entry = 80
    x_lb = 10
    global document
    document = Document("C:/Users/user/OneDrive/Desktop/Procurações/PROCURAÇÃO ENEL CNPJ.docx") 

    def inserir_entry(self,janela1,x1,y1,width1):
    
        a = tk.Entry(janela1,width=width1)
        a.place(x=x1,y=y1)
        
        return a
    
    # return a
    
    def inserir_name_label(self,janela1,x1,y1,text1):    
        
        
        Label(janela1, text=text1).place(x=x1,y=y1)
  
    
    def buscar_cnpj(self):
        # print(self.tb_CNPJ)
        cnpjSoNumeros = self.tb_CNPJ.get()
        cnpjSoNumeros = re.sub('[^0-9]', '', cnpjSoNumeros)
        c = busca_cnpj(cnpjSoNumeros)

        
        
        nomeEmpresa = json.dumps(c.nome)
        nomeEmpresa = nomeEmpresa[1:-1]

        logradouroEmpresa = json.dumps(c.logradouro)
        logradouroEmpresa = logradouroEmpresa[1:-1]
        
        numeroEmpresa = json.dumps(c.numero)
        numeroEmpresa = numeroEmpresa[1:-1]
        
        bairroEmpresa = json.dumps(c.bairro)
        bairroEmpresa =bairroEmpresa[1:-1]
        
        municipioEmpresa = json.dumps(c.municipio)
        municipioEmpresa = municipioEmpresa[1:-1]
        
        cepEmpresa = json.dumps(c.cep)
        cepEmpresa =cepEmpresa[1:-1]
        
        complementoEmpresa =json.dumps(c.complemento)
        complementoEmpresa =complementoEmpresa[1:-1]
        
        self.tb_nome_empresa.delete(0,"end")
        self.tb_Logradouro.delete(0, "end")
        self.tb_Numero.delete(0, "end")
        self.tb_cidade.delete(0, "end")
        self.tb_Bairro.delete(0,"end")
        self.tb_CEP.delete(0,"end")
        self.tb_complemento.delete(0,"end")

        
        self.tb_nome_empresa.insert(0,nomeEmpresa)  
        self.tb_Logradouro.insert(0, logradouroEmpresa)
        self.tb_Numero.insert(0, numeroEmpresa)
        self.tb_cidade.insert(0, municipioEmpresa)
        self.tb_Bairro.insert(0, bairroEmpresa)
        self.tb_CEP.insert(0, cepEmpresa)
        self.tb_complemento.insert(0,complementoEmpresa)

    def bt_inserir(self):
     for paragraph in document.paragraphs:
        
        nome_empresa_entry = self.tb_nome_empresa.get()
        
        cnpj_entry = self.tb_CNPJ.get()
        nome_entry = self.tb_nome.get()
        # print(nome_entry)
        Nacionalidade_entry = self.tb_Nacionalidade.get()
        profissao_entry = self.tb_profissao.get()
        
        ###### CPF #######
        
        
        
        cpf_entry = self.tb_cpf.get()      
        cpf = '{}.{}.{}-{}'.format(cpf_entry[:3], cpf_entry[3:6], cpf_entry[6:9], cpf_entry[9:])
        #print(cpf)
        
        ###################
        
        rg_entry = self.tb_rg.get()
        Logradouro_entry = self.tb_Logradouro.get()
        Numero_entry = self.tb_Numero.get()
        Complemento_entry = self.tb_complemento.get()
        CEP_entry = self.tb_CEP.get()
        Cidade_entry = self.tb_cidade.get()
        Bairro_entry = self.tb_Bairro.get()
        
        
        paragraph.text = paragraph.text.replace("@Empresa",nome_empresa_entry)
        paragraph.text =paragraph.text.replace("@CNPJ", cnpj_entry)
        paragraph.text = paragraph.text.replace("@Nome",nome_entry)
        paragraph.text = paragraph.text.replace("@NACIONALIDADE",Nacionalidade_entry)
        paragraph.text = paragraph.text.replace("@PROFISSAO",profissao_entry)
        paragraph.text = paragraph.text.replace("@CPF",cpf)
        paragraph.text = paragraph.text.replace("@RG ",rg_entry)
        
        if (Complemento_entry != ""):
            paragraph.text = paragraph.text.replace("@ENDERECO ",Logradouro_entry+" - " + Numero_entry+" - "+ Complemento_entry +" - " + Bairro_entry+" - " + Cidade_entry)
            print(Complemento_entry)
        else:
            paragraph.text = paragraph.text.replace("@ENDERECO ",Logradouro_entry+" - " + Numero_entry+" - " + Bairro_entry+" - " + Cidade_entry)
            
        
        
        paragraph.text = paragraph.text.replace("@CEP",CEP_entry)
        
        nome_arquivos_existentes = os.listdir('C:/Users/user/OneDrive/Desktop/Projetos-Cad')
        
        path ='C:/Users/user/OneDrive/Desktop/Procurações/'+"Procuração-"+nome_entry+".docx"
        
        if path in nome_arquivos_existentes:
            os.remove(path)
            document.save('C:/Users/user/OneDrive/Desktop/Procurações/'+"Procuração-"+nome_entry+".docx")
        else: 
            document.save(path)
    # def janela_pessoa_fisica():
    def __init__(self):
        janela_pessoa_fisica = tk.Tk()
        
        janela_pessoa_fisica.geometry("500x500+200+100")
        janela_pessoa_fisica.title("Procuração Pessoa Juridica")
        
        lb_nome_empresa = self.inserir_name_label(janela_pessoa_fisica,x_lb, 10, "Nome da empresa, adcione também o porte da mesma: ")
        
        self.tb_nome_empresa = self.inserir_entry(janela_pessoa_fisica,x_lb, 30,50)
        
        
        lb_cnpj = self.inserir_name_label(janela_pessoa_fisica,x_lb, 60, "CNPJ: ")
        
        self.tb_CNPJ = self.inserir_entry(janela_pessoa_fisica,x_entry, 60,30)
        
        bt_busca_cnpj = Button(janela_pessoa_fisica,width=20, text="buscar CNPJ", command = self.buscar_cnpj)
        bt_busca_cnpj.place(x=280,y=55)
        self.lb_Logradouro = self.inserir_name_label(janela_pessoa_fisica,x_lb, 90, "Logradouro")
        self.tb_Logradouro= self.inserir_entry(janela_pessoa_fisica,x_entry, 90, 45)
        
        lb_Numero = self.inserir_name_label(janela_pessoa_fisica,350, 90, "Número")
        self.tb_Numero= self.inserir_entry(janela_pessoa_fisica,400, 90, 10)
        
        lb_complemento = self.inserir_name_label(janela_pessoa_fisica,x_lb, 120, "Complemento")
        self.tb_complemento= self.inserir_entry(janela_pessoa_fisica,x_entry+15, 120, 30)
        
        lb_Bairro = self.inserir_name_label(janela_pessoa_fisica,x_lb, 150, "Bairro")
        self.tb_Bairro= self.inserir_entry(janela_pessoa_fisica,x_entry, 150, 30)
        
        lb_Cidade = self.inserir_name_label(janela_pessoa_fisica,x_lb, 180,"Cidade")
        self.tb_cidade = self.inserir_entry(janela_pessoa_fisica,x_entry, 180, 20)
        
        lb_CEP = self.inserir_name_label(janela_pessoa_fisica,x_lb, 210, "CEP")
        self.tb_CEP= self.inserir_entry(janela_pessoa_fisica,x_entry, 210, 15)
        
        
        lb_Dados_representante = self.inserir_name_label(janela_pessoa_fisica, x_lb, 230, "DADOS DO REPRESENTANTE")
        
        lb_nome = self.inserir_name_label(janela_pessoa_fisica,x_lb, 260, "Nome: ")
        
        self.tb_nome = self.inserir_entry(janela_pessoa_fisica,x_entry, 260,50)
        
        
        lb_Nacionalidade = self.inserir_name_label(janela_pessoa_fisica,x_lb, 290, "Nacionalidade")
        self.tb_Nacionalidade = self.inserir_entry(janela_pessoa_fisica,100, 290, 20)
        
        lb_profissao = self.inserir_name_label(janela_pessoa_fisica,x_lb, 320, "Profissão")
        self.tb_profissao= self.inserir_entry(janela_pessoa_fisica,x_entry, 320, 20)
        
        lb_cpf = self.inserir_name_label(janela_pessoa_fisica,x_lb, 350, "CPF")
        self.tb_cpf= self.inserir_entry(janela_pessoa_fisica,x_entry, 350, 20)
        
        lb_rg = self.inserir_name_label(janela_pessoa_fisica,x_lb, 380, "RG")
        self.tb_rg= self.inserir_entry(janela_pessoa_fisica,x_entry, 380, 20)
        
        
        bt_inseir = Button(janela_pessoa_fisica, width=15, text="Inserir", command=self.bt_inserir)
        bt_inseir.place(x=25,y=420)
