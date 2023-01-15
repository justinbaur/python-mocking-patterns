import requests
import json
from rich import print
from typing import Any
from pokedex.config.app_config import pokedex_api_url

class PokemonService:

    def __init__(self) -> None:
        self.pokeapi_url = pokedex_api_url

    def get_pokedex_entry(self, name: str) -> dict[str, Any]:
        """
        Return a Pokedex entry from the public API based on the Pokemon's common name
        """
        pokedex_entry = {}
        response = requests.get(f"{self.pokeapi_url}{name}")
        if response.status_code == 200:
            pokedex_entry: dict[str, Any] = response.json()
        else:
            print("[red]Failed to load Pokedex![/red]")
        return pokedex_entry

    def get_save_file(self) -> dict:
        """
        Load save data from disk
        """
        with open("save.json") as file:
            save_file = json.load(file)
        return save_file