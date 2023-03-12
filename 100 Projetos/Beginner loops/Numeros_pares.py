soma=0

for n in range(101):
    if (n%2)==0:
        soma+=n
    else:
        continue

print(f'A soma dos números pares é: {soma}')