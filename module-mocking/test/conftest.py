import os
from typing import Generator

import pytest
from pytest_mock import MockerFixture

os.environ["API_URL"] = "foo"

from pokedex.service.display_service import DisplayService  # noqa: E402 Required ordering to set test environment variable
from pokedex.service.pokemon_service import PokemonService  # noqa: E402
from pokedex.service.save_service import SaveService  # noqa: E402


@pytest.fixture
def pokemon_service(mocker: MockerFixture) -> Generator[PokemonService, None, None]:
    mocker.patch("pokedex.config.app_config.load_language_translations")
    yield PokemonService()


@pytest.fixture
def display_service(mocker: MockerFixture) -> Generator[DisplayService, None, None]:
    mocker.patch("pokedex.service.display_service.PokemonService")
    yield DisplayService()


@pytest.fixture
def save_service() -> Generator[SaveService, None, None]:
    yield SaveService()
