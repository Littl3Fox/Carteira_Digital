### Classe Carteira
#
#Objetivo: Criar um objeto capaz de armazenar as operações feitas e o montante final,
#preço médio,ganho/perda com cada operação,nome,símbolo,proventos e taxas  de determindo ativo.
#
#

#Aqui eu importo as classes e livrarias necessárias para esse Classe.

from logging import exception
from Classes.acao import Acao
from datetime import date
from Utils import utils


class Carteira:

    ## Construtor
    #Inicializa uma lista com os ativos que serão arquivados na carteira.
    def __init__(self,nome):
        self.nome=nome
        self.fiis=[]
        self.criptos=[]
        self.acoes=[]
    
    #Função "resumo"
    #
    #Objetivo: Mostrar as operações armazenadas na carteira.
    #
    #Entrada: None
    #
    #Saída: As operações armazenadas na carteira de determinado ativo

    def resumo(self):
        for acoes in self.acoes:
            print(acoes.dados())
       
    #Função "cadastra_acao"
    #
    #Objetivo: Cadastrar uma operação de compra ou venda de uma ação.
    #
    #Entrada: Data da operação, nome da empresa da ação, símbolo que representa a ação na bolsa,
    #preço de cada ação, quantidade comprada/vendida, tipo de operação(compra/venda), taxa da operação.
    #
    #Saída: Uma mensagem dizendo se a operação foi bem sucedida ou não.

    def cadastra_acao(self):
        flag=1
        try:
            data= date.fromisoformat(str(input("Digite a data da operacao(YYYY-MM-DD):")))
            nome_acao= str(input("Digite o nome da Empresa:"))
            simbolo= str(input("Digite o simbolo da Ação:"))
            ppa= float(input("Digite o preço da Ação:"))
            qnt= int(input("Digite a quantidade:"))
            op= str(input("Digite a Operação(C/V):"))
            taxa=float(input("Digite o valor da taxa, 0 se não tiver:"))
            utils.verifica_acao(nome_acao,simbolo,ppa,qnt,op,taxa)
            flag=1
        except Exception as msg:
            print(msg)
            flag=0
        else:

            print(f"Os dados:\
                Data:{data}\
                Nome da Empresa:{nome_acao}\
                Simbolo:{simbolo}\
                Preço por Ação:{ppa}\
                Quantidade:{qnt}\
                Operação:{op}\
                Taxas operacionais:{taxa}\
                Estão Corretos(S/N)?",sep="\n")
            checagem = str(input())
            if checagem =="S":
                acao=Acao(nome_acao,simbolo,qnt,ppa,op,taxa,data)
                self.acoes.append(acao)
            else:
                flag=0
            
        finally:
            if flag == 0:
                print("Operação falhou!")
            else:
                print("Operação cadastrada com sucesso")

        

