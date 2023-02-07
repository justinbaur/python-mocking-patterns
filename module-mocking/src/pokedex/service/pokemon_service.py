import httpx
from rich import print
from typing import Any
from pokedex.config.app_config import pokedex_api_url, load_language_translations

class PokemonService:

    def __init__(self) -> None:
        self.pokeapi_url = pokedex_api_url
        load_language_translations()

    def get_pokemon(self, name: str) -> dict[str, Any]:
        """
        Return a Pokedex entry from the Pokemon's common name
        """
        pokedex_entry = {}
        response = httpx.get(f"{self.pokeapi_url}/pokemon/{name}")
        if response.status_code == 200:
            pokedex_entry: dict[str, Any] = response.json()
        else:
            print("[red]Failed to load pokemon from pokedex![/red]")
        return pokedex_entry

    def get_pokemon_species(self, id: int) -> dict[str, Any]:
        """
        Return a Pokedex entry from the Pokemon's common name
        """
        species_entry = {}
        response = httpx.get(f"{self.pokeapi_url}/pokemon-species/{id}")
        if response.status_code == 200:
            species_entry: dict[str, Any] = response.json()
        else:
            print("[red]Failed to load pokemon species from pokedex![/red]")
        return species_entry

    def get_region(self, name: str) -> dict:
        """
        Return a region entry 
        """
        region_entry = {}
        response = httpx.get(f"{self.pokeapi_url}/region/{name}")
        if response.status_code == 200:
            region_entry: dict[str, Any] = response.json()
        else:
            print("[red]Failed to load region from pokedex![/red]")
        return region_entry

    def get_loction_area(self, name: str) -> dict:
        """
        Return a region entry 
        """
        location_area_entry = {}
        response = httpx.get(f"{self.pokeapi_url}/location-area/{name}")
        if response.status_code == 200:
            location_area_entry: dict[str, Any] = response.json()
        else:
            print("[red]Failed to load location entry from pokedex![/red]")
        return location_area_entry
