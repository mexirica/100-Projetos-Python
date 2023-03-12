altura=input("Escreva as altura em cm separadas por um espaço.").split()
soma=0
for n in altura:
    soma+=int(n)

print(f'A média das alturas é {soma/(len(altura))}')