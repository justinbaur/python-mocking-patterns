import json

class SaveService:

    def get_save_file(self) -> dict: 
        """
        Load save data from disk
        """
        with open("save.json") as file:
            save_file = json.load(file)
        return save_file