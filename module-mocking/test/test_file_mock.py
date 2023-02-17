from pytest_mock import MockerFixture

from pokedex.service import save_service


class TestSaveFile:

    def test_save_file(self, save_service: save_service.SaveService, mocker: MockerFixture) -> None:
        """
        Blah
        """
        mock_save = '{"foo": "bar"}'  # noqa: FS003 Double quotes required for JSON key values
        mock_file = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_save))

        save_file = save_service.get_save_file()

        assert save_file == { "foo": "bar"}
        mock_file.call_count == 1
        mock_file.reset_mock()
