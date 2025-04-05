from pydantic import BaseModel, RootModel


class EntityIdModel(RootModel):

    root: int


class AdditionModel(BaseModel):

    id: int
    additional_info: str
    additional_number: int


class EntityModel(BaseModel):

    id: int
    title: str
    verified: bool
    addition: AdditionModel
    important_numbers: list[int]


class EntitiesModel(BaseModel):

    entity: list[EntityModel]


class EntityDateModel(BaseModel):

    Date: str
