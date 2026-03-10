name: str = "Maria"
age: int = 22
height: float = 1.68
is_student: bool = True

print(f"Name: {name} | Type: {type(name)}")
print(f"Age: {age} | Type: {type(age)}")
print(f"Height: {height} | Type: {type(height)}")
print(f"Is Student: {is_student} | Type: {type(is_student)}")

name = input("\nYour name: ")
weight: int = int(input("Your weight (kg): "))
height_user: float = float(input("Your height (m): "))

imc: float = weight / (height_user * height_user)

print(f"\nIMC: {imc:.2f}")
