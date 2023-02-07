from pokedex.service.pokemon_service import PokemonService

class DisplayService:

    def __init__(self) -> None:
        self.pokemon_service = PokemonService()

    def display_pokedex_entry(self, name: str) -> None:
        """
        Format and display a Pokedex entry 
        """
        pokedex_entry = self.pokemon_service.get_pokedex_entry(name)
        pokemon_name = pokedex_entry.get("name", "unknown")
        pokedex_number = pokedex_entry.get("id", -1)

        print(f"[blue]Pokedex Entry {pokedex_number}[/blue]")
        print(f"[green]Name: {pokemon_name}[/green]")

        self.display_pokemon_species()

    def display_pokemon_species(self, id: int) -> None:
        """
        blah
        """
        species_entry = self.pokemon_service.get_pokemon_species(id)
        color = species_entry.get("color", {})

        print(f"[green]Color: {color.get('name', '')}[/green]")