import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

seu=int(input("Digite 0 para pedra, 1 para papel e 2 para tesoura.\n"))

escolhas=[pedra, papel, tesoura]

oponente=random.randint(0,len(escolhas) -1)

print(f'Sua escolha:\n{escolhas[seu]}')

print(f'Escolha do seu oponente:\n{escolhas[oponente]}')

if seu==oponente:
    print("Empate")
elif seu>oponente:
    print('Você ganhou')
elif seu<oponente:
    print("Você perdeu")
elif seu==0 and oponente==2:
    print('Você ganhou')
elif oponente==0 and seu==2:
    print("Você perdeu")
elif seu>=3 or seu<0:
    print('Opção inválida')