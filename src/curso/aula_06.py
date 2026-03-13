# WHILE: números de 1 a 10
number: int = 1
while number <= 10:
    print(number)
    number += 1


# FOR: números de 1 a 10
for i in range(1, 11):
    print(i)


# TABUADA
number: int = int(input("\nDigite um número para a tabuada: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


# CONTADOR REGRESSIVO
start: int = int(input("\nDigite o número inicial da contagem regressiva: "))
while start > 0:
    print(start)
    start -= 1

print("Fogo!")
