#!/usr/bin/env python3

import json
import sys
import urllib.request

class busca_cnpj():
    
    def __init__(self,cnpj):
        url = 'http://receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-agent',
             " Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0")]
    
        with opener.open(url) as fd:
            content = fd.read().decode()
    
        dic = json.loads(content)
    
        if dic['status'] == "ERROR":
            print('CNPJ {0} rejeitado pela receita federal\n\n'.format(cnpj))
        else:
            try:
                print('Nome: {0}'.format(dic['nome']))
                print('Nome fantasia: {0}'.format(dic['fantasia']))
                print('CNPJ: {0}   Data de abertura: {1}'.format(dic['cnpj'], dic['abertura']))
                print('Natureza: {0}'.format(dic['natureza_juridica']))
                print('Situação: {0}  Situação especial: {1}  Tipo: {2}'.format(dic['situacao'],
                                                                                dic['situacao_especial'],
                                                                                dic['tipo']))
                print('Motivo Situação especial: {0}'.format(dic['motivo_situacao']))
                print('Data da situação: {0}'.format(dic['data_situacao']))
                print('Atividade principal:')
                print(' '*10 + '{0} - {1}'.format(dic['atividade_principal'][0]['code'],
                                                  dic['atividade_principal'][0]['text']))
                print('Atividades secundárias:')
                for elem in dic['atividades_secundarias']:
                    print(' '*10 + '{0} - {1}'.format(elem['code'], elem['text']))
    
                print('Endereço:')
                print(' '*10 + '{0}, {1}'.format(dic['logradouro'],
                                                 dic['numero']))
            
                self.logradouro = ('{0}'.format(dic['logradouro']))
                self.numero = ('{0}'.format(dic['numero']))
                self.nome = ('{0}'.format(dic['nome']))
                self.complemento = ('{0}'.format(dic['complemento'])) 
                self.municipio = ('{0}'.format(dic['municipio']))
                
                self.bairro = ('{0}'.format(dic['bairro'])) 
                self.cep = ('{0}'.format(dic['cep'])) 
                print(' '*10 + '{0}'.format(dic['complemento']))
                print(' '*10 + '{0}, {1}'.format(dic['municipio'],
                                                 dic['uf']))
                print('Telefone: {0}'.format(dic['telefone']))
                print('Email: {0}\n\n'.format(dic['email']))
                print('Email: {0}\n\n'.format(dic['bairro']))
                print('Email: {0}\n\n'.format(dic['cep']))
            except KeyError:
                pass
            
        
    
    def passaN(self):
        
        
        return self.logradouro,self.municipio,self.nome,self.numero,self.bairro,self.cep,self.complemento




