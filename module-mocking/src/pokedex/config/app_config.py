import os
from dotenv import load_dotenv

load_dotenv()

pokedex_api_url = os.getenv("API_URL")

def get_default_region() -> str:
    return "kanto"