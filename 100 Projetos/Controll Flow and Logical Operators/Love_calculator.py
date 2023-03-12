nome1=input("Escreva seu nome: ")
nome2=input("Escreva o nome da outra pessoa: ")

combinado=nome1+nome2
combinado=combinado.lower()

t=combinado.count("t")
r=combinado.count("r")
u=combinado.count("u")
e=combinado.count("e")

true=t+r+u+e

l=combinado.count("l")
o=combinado.count("o")
v=combinado.count("v")

love=l+o+v+e

total=str(true) + str(love)
total=int(total)

if total<10 or total>90:
    print(f"Sua pontuação é de {total}, vocês combinam igual gato e rato!")
elif total>40 and total>50:
    print(f"Sua pontuação é de {total}, vocês se dão bem!")
else:
    print(f"Sua pontuação é de {total}")