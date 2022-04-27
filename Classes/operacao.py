#Aqui eu decedi que faz mais sentido ter uma classe operações e a partir das operações registradas
#dizer quais ativos fazem parte da carteira e quais não fazem mais parte

#Variáveis Globais



id=0  #Vai ser utilizado para identificar as várias operações

#Classe

class Operacao:
    
    def __init__(self,data,nome_ativo,simbolo,ppa,quantidade,op,tipo,taxas):
        global id
        self.identificador = id
        self.data=data
        self.nome=nome_ativo
        self.simbolo=simbolo
        self.ppa=ppa
        self.quantidade=quantidade
        self.op=op
        self.tipo=tipo
        self.taxa=taxas
        id+=1
        pass


    def get_id(self):
        return self.identificador 

    def get_data(self):
        return self.data

    def get_nome(self):
        return self.nome 

    def get_simbolo(self):
        return self.simbolo  

    def get_ppa(self):
        return self.ppa 

    def get_quantidade(self):
        return self.quantidade

    def get_operacao(self):
        return self.op

    def get_tipo(self):
        return self.tipo 

    def get_taxa(self):
        return self.taxa  