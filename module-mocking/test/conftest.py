import os

import pytest
from pytest_mock import MockerFixture

os.environ["API_URL"] = "foo"

from pokedex.service.pokemon_service import PokemonService
from pokedex.service.display_service import DisplayService
from pokedex.service.save_service import SaveService

@pytest.fixture
def pokemon_service(mocker: MockerFixture) -> PokemonService:
    mocker.patch("pokedex.service.pokemon_service.PokemonService.load_language_translations")
    yield PokemonService()

@pytest.fixture
def display_service() -> DisplayService:
    yield DisplayService()

@pytest.fixture
def save_service() -> SaveService:
    yield SaveService()