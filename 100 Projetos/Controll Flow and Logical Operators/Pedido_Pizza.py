print("Bem-vindo a nossa pizzaria!")

tamanho=(input("Qual tamanho você deseja ? \n P,M ou G ?"))
pepperoni=input("Você quer pepperoni ? \n S ou N ?")
queijo=input("Deseja queijo extra ? \n S ou N ?")

soma=0

if tamanho == "S":
    soma=15
elif tamanho == "M":
    soma+=20
elif tamanho == "G":
    soma=25

if pepperoni == "S":
    if tamanho == "S":
        soma+=1
    else:
        soma+=2

if queijo == "S":
    soma+=1

print(f"O valor do seu pedido é de {soma}")