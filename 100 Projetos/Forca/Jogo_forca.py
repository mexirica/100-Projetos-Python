import random

palavras=["abacaxi", "macaco", "pessoa"]

vidas=6

palavra=random.choice(palavras)

teste=[]

for n in range(len(palavra)):
    teste+='_'

game_over=False


while not game_over:
    letra = input("Digite uma letra: ").lower()
    if letra in teste:
        print(f'Você já adivinhou {letra}')
    for n in range(len(palavra)):
        posicao=palavra[n]
        if posicao==letra:
            teste[n]=posicao
    print(f"{' '.join(teste)}")
    if '_' not in teste:
        game_over=True
        print("Você ganhou")
    if letra not in palavra:
        vidas-=1
        print(f'Vidas= {vidas}')
        if vidas==0:
            print('Você perdeu')
            break;

    from hangman_art import stages
    print(stages[vidas])