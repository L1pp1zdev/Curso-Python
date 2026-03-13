a: int = 15
b: int = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

print(a > b)
print(a == b)
print(a != b)

n: int = int(input("Digite um número inteiro: "))
is_even: bool = n % 2 == 0
print(f"O número {n} é par? {is_even}")
