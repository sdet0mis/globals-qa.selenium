from typing import Any

from faker import Faker


class EntityData:

    def entity(self) -> tuple[Any]:
        return (
            Faker().pystr(),
            Faker().pyint(),
            Faker().pylist(3, value_types=int),
            Faker().pystr(),
            Faker().pybool()
        )
