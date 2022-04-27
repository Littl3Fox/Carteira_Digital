import string


def verifica_acao(nome_acao,simbolo,ppa,qnt,op,taxa):

    if not(nome_acao.isprintable() and nome_acao.isalnum()):

        raise ValueError("Nome incorreto!")

    if not(simbolo.isprintable() and simbolo.isalnum()):

        raise ValueError("Simbolo incorreto!")
    
    if not(ppa>=0):

        raise ValueError("Preço por ação incorreto!")

    if not( qnt>=0):

        raise ValueError("Quantidade incorreta!")
    if not(op.isalpha() or (op.upper()=="C" or op.upper()=="V")):

        raise ValueError("Operação incorreta!")
    if not(taxa>=0):

        raise ValueError("Taxa incorreta!")
   


