user = {}

name: str = input("Digite o nome: ")
age: int = int(input("Digite a idade: "))
city: str = input("Digite a cidade: ")

user["name"] = name
user["age"] = age
user["city"] = city

print("\nUsuário cadastrado:\n")

for key, value in user.items():
    print(f"{key}: {value}")
