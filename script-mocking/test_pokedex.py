from pokedex import get_pokedex_entry

class MockResponse:

    def __init__(self, status_code: int, json_data: dict = None, text: str = None) -> None:
        self.status_code = status_code
        self.json_data = json_data
        self.text = text

    def json(self) -> dict:
        return self.json_data


def test_get_ok(mocker) -> None:
    input = "weedle"
    expected_response = {"name": "weedle", "id": 13}

    mocker.patch("pokedex.requests.get", return_value=MockResponse(200, expected_response))
    
    actual_response = get_pokedex_entry(input)

    assert actual_response.get("name") == input, 'incorrect pokedex name'
    assert actual_response == expected_response, 'incorrect pokedex entry'