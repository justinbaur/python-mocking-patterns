# Module

## Overview

This pattern shows the use of mocking with from within a built Python module.

## Setup

> Make sure to have changed directories in your terminal to `module-mocking` before running commands.

1. Run the setup script: `source venv.sh`

## Tests

Execute tests with Tox: `tox`

## Mocks

- Mocking methods internal to your class
  - `display_service.py` usage of `
- Mocking decorators
- Mocking files
  - `pokedex_service.py` usage of `save.json`
- Mocking library imports
  - `pokedex_service.py` usage of httpx
- Mocking non class modules imports
  - `pokedex_service.py` usage of `get_default_region` from `app_config.py`
- Mocking env variables
  - `pokedex_service.py` usage of `pokedex_api_url`
- Mock before a yield of a class

## Bonus mocking content

- Mock subprocess CalledProcessError with stderr
