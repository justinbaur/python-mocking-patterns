# Module Mocking

## Overview

This pattern shows the use of mocking with from within a built Python module.

## Setup

> Make sure to have changed directories in your terminal to `module-mocking` before running commands.

1. Run the setup script: `source venv.sh`

## Tests

Execute tests with Tox: `tox`

## Mock Descriptions

Test mocking methods internal to your class

- Description
  - `display_service.py` usage of the `display_pokedex_entry` method calling `display_pokemon_species`
- Test Location
  - `module-mocking/test/test_class_mock.py`

Test mocking a file

- Description
  - `save_service.py` usage of `save.json`
- Test Location
  - `module-mocking/test/test_file_mock.py`

Mocking library imports

  - `pokedex_service.py` usage of httpx
- Mocking non class modules imports
  - `pokedex_service.py` usage of `get_default_region` from `app_config.py`
- Mocking env variables
  - `pokedex_service.py` usage of `pokedex_api_url`
- Mock before a yield of a class
  - `pokemon_service.py` usage of `app_config.py` method `load_language_translations`
- Mocking decorators

## Bonus mocking content

- Mock subprocess CalledProcessError with stderr
