from dataclasses import dataclass


@dataclass
class Addition:

    additional_info: str
    additional_number: int


@dataclass
class Entity:

    addition: Addition
    important_numbers: list[int]
    title: str
    verified: bool
