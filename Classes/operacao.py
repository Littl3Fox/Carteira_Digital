#Aqui eu decedi que faz mais sentido ter uma classe operações e a partir das operações registradas
#dizer quais ativos fazem parte da carteira e quais não fazem mais parte

#Variáveis Globais

id=0  #Vai ser utilizado para identificar as várias operações

#Classe

class Operacao:
    
    def __init__(self,data,nome_ativo,simbolo,ppa,quantidade,tipo,taxas):
        global id
        self.identificador = id
        self.data=data
        self.nome=nome_ativo
        self.simbolo=simbolo
        self.ppa=ppa
        self.quantidade=quantidade
        self.tipo=tipo
        self.taxa=taxas
        id+=1
        pass
    
  