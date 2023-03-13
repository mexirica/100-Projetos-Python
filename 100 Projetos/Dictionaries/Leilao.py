def leilao():
    lances={}
    pessoas=True
    while pessoas==True:
        nome=input("Qual o seu nome ?")
        valor=int(input(("Qual o seu lance ?")))
        lances[nome]=valor
        mais_lances=input("Tem mais pessoas querendo dar lances ? Digite 'sim' ou 'nao'").lower()
        if mais_lances=='sim':
            leilao()
        else:
            max_value = list(lances.values())
            max_key = list(lances.keys())
            print(f'O vencedor do lance é {max_key[max_value.index(max(max_value))]} com o lance de {(max_value[max_value.index(max(max_value))])}')
        pessoas=False

leilao()