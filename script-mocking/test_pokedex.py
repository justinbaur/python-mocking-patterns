from pokedex import get_pokedex_entry

def test_get_ok():
    expected_response = {"name": "weedle", "id": 13}
    actual_response = get_pokedex_entry("weedle")
    assert actual_response == expected_response