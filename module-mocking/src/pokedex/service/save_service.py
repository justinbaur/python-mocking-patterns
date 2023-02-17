import json
from typing import Any


class SaveService:

    def get_save_file(self) -> dict[str, Any]:
        """
        Load save data from disk
        """
        with open("save.json") as file:
            save_file: dict[str, Any] = json.load(file)
        return save_file
