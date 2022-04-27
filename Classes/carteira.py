### Classe Carteira
#
#Objetivo: Criar um objeto capaz de armazenar as operações feitas e o montante final,
#preço médio,ganho/perda com cada operação,nome,símbolo,proventos e taxas  de determindo ativo.
#
#

#Aqui eu importo as classes e livrarias necessárias para esse Classe.

from logging import exception
from Classes import operacao
from datetime import date
from Utils import utils


#Variáveis globais
operacoes=[]

class Carteira:

    ## Construtor
    #Inicializa uma lista com os ativos que serão arquivados na carteira.
    def __init__(self,nome):
        self.nome=nome
        
    #Função "cadastra_acao"
    #
    #Objetivo: Cadastrar uma operação de compra ou venda de uma ação.
    #
    #Entrada: Data da operação, nome da empresa da ação, símbolo que representa a ação na bolsa,
    #preço de cada ação, quantidade comprada/vendida, tipo de operação(compra/venda), taxa da operação.
    #
    #Saída: Uma mensagem dizendo se a operação foi bem sucedida ou não.

    def cadastra_operacao(self):
        flag=1
        try:
            data= date.fromisoformat(str(input("Digite a data da operacao(YYYY-MM-DD):")))
            nome_ativo= str(input("Digite o nome do Ativo/Empresa:"))
            simbolo= str(input("Digite o simbolo do Ativo:"))
            ppa= float(input("Digite o preço unitário do ativo:"))
            qnt= float(input("Digite a quantidade:"))
            op= str(input("Digite a Operação(C/V):"))
            tipo = str(input("Digite o tipo de ativo(Cripto,Ação,FII,etc...):"))
            taxa=float(input("Digite o valor da taxa, 0 se não tiver:"))
            utils.verifica_acao(nome_ativo,simbolo,ppa,qnt,op,taxa)
            flag=1
        except Exception as msg:
            print(msg)
            flag=0
        else:

            print(f"Os dados:\
                Data:{data}\
                Nome da Empresa:{nome_ativo}\
                Simbolo:{simbolo}\
                Preço por ativo:{ppa}\
                Quantidade:{qnt}\
                Operação:{op}\
                Tipo:{tipo}\
                Taxas operacionais:{taxa}\
                Estão Corretos(S/N)?",sep="\n")
            checagem = str(input())
            if checagem =="S":
                ope=operacao.Operacao(data,nome_ativo,simbolo,ppa,qnt,op,tipo,taxa)
                global operacoes
                operacoes.append(ope)
            else:
                flag=0
            
        finally:
            if flag == 0:
                print("Operação falhou!")
            else:
                print("Operação cadastrada com sucesso")

    #Função "mostra_operacoes"
    #
    #Objetivo: Mostrar as operações armazenadas na carteira.
    #
    #Entrada: None
    #
    #Saída: As operações armazenadas na carteira de determinado ativo

    def mostra_operacoes(self):
        global operacoes
        print("Operações:\n")
        for obj in operacoes:
           print(f"Identificador:{obj.get_id()}\
                Data:{obj.get_data()}\
                Nome:{obj.get_nome()}\
                Simbolo:{obj.get_simbolo()}\
                Preço unitário:{obj.get_ppa()}\
                Quantidade:{obj.get_quantidade()}\
                Operação:{obj.get_operacao()}\
                Tipo de ativo:{obj.get_tipo()}\
                Taxas:{obj.get_taxa()}\  ",sep="\n")

        

