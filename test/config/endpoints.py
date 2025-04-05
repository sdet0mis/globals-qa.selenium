BASE_URL = "http://localhost:8080/api"


class EntityEndpoints:

    CREATE_ENTITY = f"{BASE_URL}/create"
    DELETE_ENTITY = lambda self, id: f"{BASE_URL}/delete/{id}"  # noqa
    GET_ENTITY = lambda self, id: f"{BASE_URL}/get/{id}"  # noqa
    GET_ENTITIES = f"{BASE_URL}/getAll"
    UPDATE_ENTITY = lambda self, id: f"{BASE_URL}/patch/{id}"  # noqa
