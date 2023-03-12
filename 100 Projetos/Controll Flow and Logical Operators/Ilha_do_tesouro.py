print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo a Ilha do Tesouro")
print("Sua missão é acha-lo")

escolha1=input("Você tá em uma encruzilhada, vai para direita ou esquerda ?\n")

if escolha1=="esquerda":
    escolha2=input('Você chegou a um lago, tem uma pequena ilha no meio dele. Digite "esperar" para esperar por um barco ou digite "nadar" para nadar até a ilha:\n').lower()
    if escolha2== "esperar":
        escolha3=  input('Você chegou na ilha. Nela tem uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Escolha uma porta\n').lower()
        if escolha3=="vermelha":
            print("Você entrou em uma sala cheia de fogo.\nGame over!")
        elif escolha3=="amarela":
            print('Você achou o tesouro!')
        elif escolha3=="azul":
            print('Você entrou em uma sala cheia de animais selvagens.\nGame over!')
        else:
            print('Você escolheu uma porta que não existe')
    else:
        print("Você foi atacado por uma truta e morreu")
else:
    print("Você caiu em um buraco e morreu")
