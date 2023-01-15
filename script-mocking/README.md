# Script

## Overview

This pattern shows the use of mocking with a single Python file and not bundled in your own Python package.  The mock works by changing the response object that the name `pokedex.requests.get` points to with the `MockResponse` class.

## Setup

> Make sure to have changed directories in your terminal to `script-mocking` before running commands. Commands assume Windows with Git Bash.

1. Create a new virtual environment: `python -m venv .venv`
1. Activate it: `source .venv/Scripts/activate`
1. Install dependencies: `pip install -r requirements.txt`

## Tests

Execute tests using pytest by running the command: `python -m pytest`
