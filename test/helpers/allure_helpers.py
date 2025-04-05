import json

import allure
from allure_commons.types import AttachmentType
from requests import Response


class AllureHelpers:

    @staticmethod
    def attach_response_headers(response: Response) -> None:
        allure.attach(
            json.dumps(dict(response.headers), indent=4),
            "Ответ",
            AttachmentType.JSON
        )

    @staticmethod
    def attach_response_body(response: Response) -> None:
        allure.attach(
            response.content,
            "Ответ",
            AttachmentType.JSON
        )
