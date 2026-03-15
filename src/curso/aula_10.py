def greet(name: str) -> None:
    """Show a greeting."""
    print(f"Olá, {name}")


def square(number: int) -> int:
    """Return the square of a number."""
    return number**2


def is_even(number: int) -> bool:
    """Return True if the number is even."""
    return number % 2 == 0


def create_user(name: str, age: int, city: str) -> dict[str, str | int]:
    """Create a user dictionary."""
    return {
        "name": name,
        "age": age,
        "city": city,
    }


def main() -> None:
    """Program entry point."""
    name: str = input("Digite seu nome: ")
    greet(name)

    age: int = int(input("Digite sua idade: "))
    city: str = input("Digite sua cidade: ")

    user: dict[str, str | int] = create_user(name, age, city)
    print(user)

    number: int = int(input("Digite um número inteiro: "))

    result_square: int = square(number)
    print(f"Quadrado de {number} é {result_square}")

    result_is_even: bool = is_even(number)
    print(f"O número {number} é par? {result_is_even}")


if __name__ == "__main__":
    main()
