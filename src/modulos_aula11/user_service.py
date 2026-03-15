def create_user(name: str, age: int, city: str) -> dict[str, str | int]:
    #Register new user
    return {
        "name": name,
        "age": age,
        "city": city
    }
