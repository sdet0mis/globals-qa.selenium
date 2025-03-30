import random

from faker import Faker


def new_customer() -> dict[str, str]:
    post_code = "".join([str(random.randint(0, 9)) for _ in range(10)])
    numbers = [post_code[digit:digit + 2] for digit in range(0, 10, 2)]
    first_name = "".join([chr(int(number) % 26 + 97) for number in numbers])
    last_name = Faker().last_name()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "post_code": post_code
    }


def customer_to_delete(names: list[str]) -> dict[str, str]:
    names_lengths = [len(name) for name in names]
    average_length = sum(names_lengths) / len(names_lengths)
    name = min(names, key=lambda name: abs(len(name) - average_length))
    customer_id = str(names.index(name) + 1)
    return {"customer_id": customer_id, "name": name}
