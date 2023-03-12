import random

print('Bem vindo ao gerador de senhas')

n_letras=int(input('Quantas letras você deseja ? '))
n_numeros=int(input('Quantos números você deseja: '))
n_simbolos=int(input('Quantos símbolos você deseja: '))

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

senha=[]

for n in range(1,n_letras+1):
    senha.append(random.choice(letras))

for n in range(1, n_numeros+1):
    senha+=random.choice(numeros)

for n in range(1, n_simbolos+1):
    senha+=random.choice(simbolos)

random.shuffle(senha)
senha2=''

for n in senha:
    senha2+=n

print(senha2)