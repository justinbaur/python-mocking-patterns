from pytest_mock import MockerFixture

from pokedex.service import display_service


class TestDisplayService:

    def test_mock_internal_class_method(self, display_service: display_service.DisplayService, mocker: MockerFixture) -> None:
        """
        Foo
        """
        mock_pokemon_id = 69
        mock_pokemon_name = "snorlax"

        mock_get_pokemon = mocker.patch("pokedex.pokemon_service.get_pokemon")
        mock_get_pokemon.return_value = {"name": mock_pokemon_name, "id": mock_pokemon_id}

        mock_display_pokemon_species = mocker.patch("pokedex.service.display_service.DisplayService")

        display_service.display_pokedex_entry(mock_pokemon_name)

        mock_display_pokemon_species.call_count == 1
        mock_get_pokemon.assert_called_once_with(mock_pokemon_id)
        mock_get_pokemon.call_count == 1
