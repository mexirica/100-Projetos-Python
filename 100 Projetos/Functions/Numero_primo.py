def primo():
    eh_primo=True
    numero=int(input('Digite o número a ser checado: '))
    for n in range(2,numero):
        if numero % n == 0:
            eh_primo=False
    if eh_primo==True:
        print("Primo")
    else:
        print('Não é primo')

primo()