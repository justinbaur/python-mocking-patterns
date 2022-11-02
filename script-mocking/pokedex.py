import requests
from rich import print
from typing import Any

def get_pokedex_entry(name: str) -> dict[str, Any]:
    pokedex_entry = {}
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code == 200:
        pokedex_entry: dict[str, Any] = response.json()
    else:
        print("[red]Failed to load Pokedex![/red]")
    return pokedex_entry

def display_pokedex_entry(name: str) -> None:
    pokedex_entry = get_pokedex_entry(name)
    pokemon_name = pokedex_entry.get("name", "unknown")
    pokedex_number = pokedex_entry.get("id", -1)

    print(f"[blue]Pokedex Entry {pokedex_number}[/blue]")
    print(f"[blue]{pokemon_name}[/blue]")

display_pokedex_entry("weedle")