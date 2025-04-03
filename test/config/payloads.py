from typing import Any


class EntityPayloads:

    def entity(
        self,
        additional_info: str,
        additional_number: int,
        important_numbers: list[int],
        title: str,
        verified: bool
    ) -> dict[str, Any]:
        return {
            "addition": {
                "additional_info": additional_info,
                "additional_number": additional_number
            },
            "important_numbers": important_numbers,
            "title": title,
            "verified": verified
        }
