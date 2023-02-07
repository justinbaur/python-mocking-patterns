import os
from typing import Any
import httpx
from dotenv import load_dotenv

load_dotenv()

pokedex_api_url = os.getenv("API_URL")

def get_default_region() -> str:
    return "kanto"

def load_language_translations(language: str ="en") -> dict[str, Any]:
    response = httpx.get(f"{pokedex_api_url}/language/{language}")
    if response.status_code == 200:
        language_translation: dict[str, Any] = response.json()
    else:
        print("[red]Failed to load language translation![/red]")   
    return language_translation