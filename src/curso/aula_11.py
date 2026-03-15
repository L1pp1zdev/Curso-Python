from modulos_aula11.math_utils import is_even, square
from modulos_aula11.user_service import create_user


def main() -> None:
    """Program entry point."""

    name: str = input("Digite um nome: ")
    age: int = int(input("Digite sua idade: "))
    city: str = input("Digite a sua cidade: ")

    result_square: int = square(age)
    result_is_even: bool = is_even(age)
    user: dict[str, str | int] = create_user(name, age, city)

    print(f"O quadrado de {age} é {result_square}")
    print(f"O número {age} é par? {result_is_even}")
    print(f"Usuário criado: {user}")


if __name__ == "__main__":
    main()
