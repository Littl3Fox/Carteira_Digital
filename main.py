from Classes import carteira

teste= carteira.Carteira("nova_carteira")
continuar = 1
while continuar!=0:
    print("MENU\
        Digite 1 para cadastrar uma operação.\
        Digite 2 para ver as operações cadastradas.",sep="\n")
    continuar = int(input("--->"))

    if continuar == 1:
        teste.cadastra_operacao()
    elif continuar == 2:
        teste.mostra_operacoes()
    else:
        continuar=0
        continue
    
    
    