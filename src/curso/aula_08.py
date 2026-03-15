numbers = list(range(1, 21))  # numbers = [i for i in range(1, 21)]
print(numbers)

squares = [i**2 for i in range(1, 11)]
print(squares)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

numbers_bigger_than_ten = [i for i in range(1, 21) if i > 10]
print(numbers_bigger_than_ten)

numbers = []

for _ in range(10):
    n = int(input("Digite um número: "))
    numbers.append(n)

greater_than_ten = [n for n in numbers if n > 10]

print("Lista original:", numbers)
print("Maiores que 10:", greater_than_ten)
