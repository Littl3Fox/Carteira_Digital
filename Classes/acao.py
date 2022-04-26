class Acao:
    def __init__(self,nome_empresa,simbolo,qnt,preço_por_acao,operacao,taxa,data):
        self.nome=nome_empresa
        self.simbolo=simbolo
        self.qnt=qnt
        self.ppa=preço_por_acao
        self.op=operacao
        self.taxa=taxa
        self.data= data
    
    def dados(self):
        print(f"Nome:{self.nome}\
            Data:{self.data}.")

    
    
        