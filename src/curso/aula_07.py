numbers = [10, 20, 30, 40, 50]
# Mostra o Primeiro e o Último item da lista
print(numbers[0])
print(numbers[-1])

# Adicionar na lista
numbers.append(60)
print(numbers)

# Percorre a lista imprimindo seus valores
for number in numbers:
    print(number)


# O usuário cria uma lista personalizada de números e mostra
# A lista inteira, o maior e o menor valor dentro dela
user_numbers = []

i = 1
while i <= 5:
    number: int = int(input("Digite um número: "))
    user_numbers.append(number)
    i += 1

print("\nLista completa:", user_numbers)
print(f"Menor número: {min(user_numbers)}")
print(f"Maior número: {max(user_numbers)}")
