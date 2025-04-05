from faker import Faker


class EntityData:

    @staticmethod
    def entity() -> tuple[str, int, list[int], str, bool]:
        return (
            Faker().pystr(),
            Faker().pyint(),
            Faker().pylist(3, value_types=int),
            Faker().pystr(),
            Faker().pybool()
        )
