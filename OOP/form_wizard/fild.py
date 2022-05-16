from typing import Final


class Fild:
    _FILDS_CONFIGURATION: Final[dict] = {
        "phone": {
            "name": "phone",
            "type": "str",
        },
        "name": {
            "name": "name",
            "type": "str",
        },
    }

    _name = ""

    def __init__(self, name):
        self.check_name(name)

    @property
    def name(self) -> str:
        return self._name

    def check_name(self, filds_name: str) -> None:
        """Próba przypisania niewłaściwej wartości do atrybutu wywoła błąd."""
        if filds_name in self._FILDS_CONFIGURATION:
            self._name = filds_name
        else:
            raise ValueError(f"{filds_name} is an invalid value for name")

    def get_field_configuration(self) -> dict:
        return self._FILDS_CONFIGURATION.get(self.name)

    def __repr__(self):
        return f"Filds('{self._name}')"
