altura=float(input("Digite sua altura em metros: "))
peso=float(input("Digite seu peso em kg: "))

bmi=round(peso/(altura**2))

if bmi<18.5:
    print(f"Seu bmi é {bmi}, você está abaixo do peso ")
elif bmi<25:
    print(f"Seu BMI é {bmi}, você está com o peso normal")
elif bmi<30:
    print(f"Seu BMI é {bmi}, você está acima do peso")
elif bmi<35:
    print(f"Seu BMI é {bmi}, você está obeso")
elif bmi>35:
    print(f"Seu BMI é {bmi}, você é um obeso clínico")