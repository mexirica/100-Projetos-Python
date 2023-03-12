import random

nomes=input('Escreva os nomes das pessoas separados por uma vírgula.\n').split(', ')

escolhido=random.randint(0,len(nomes)-1)

print('A pessoa escolhida foi ' + nomes[escolhido])