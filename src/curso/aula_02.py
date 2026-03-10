name_system:str = "SISTEMA DE CADASTRO"
stars: str = "*" * len(name_system)


print(stars)
print(name_system)
print(stars)

name:str = input("Digite seu nome: ")
age:int = int(input("Digite sua idade: "))
city:str = input("Nome da sua cidade: ")
year_born: int = 2026 - age

print("\nUsuário Cadastrado!!!\n")

print(f"\nNome: {name}")
print(f"Idade: {age}")
print(f"Cidade: {city}")
print(f"Ano de Nascimento: {year_born}")
