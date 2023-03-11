ano=int(input("Digite o ano desejado: "))

if (ano%4) == 0:
    if (ano%100) != 0:
        print(f"O ano {ano} é bisexto")
    elif (ano%400) == 0:
        print(f"O ano {ano} é bisexto")
else:
    print(f"O ano {ano} não é bisexto")
