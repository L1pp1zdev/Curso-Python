# Verificação de idade
age: int = int(input("Digite sua idade: "))

if age >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


# Verificação de número
number: int = int(input("\nDigite um número: "))

if number > 0:
    print("Número positivo")
elif number < 0:
    print("Número negativo")
else:
    print("Número zero")


# Cálculo de IMC
weight: int = int(input("\nYour weight (kg): "))
height_user: float = float(input("Your height (m): "))

imc: float = weight / (height_user * height_user)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
