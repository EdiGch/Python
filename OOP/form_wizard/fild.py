from typing import Final


class Fild:
    FILD_PHONE: Final[str] = "phone"
    FILD_NAME: Final[str] = "name"
    _FILDS_CONFIGURATION: Final[dict] = {
        FILD_PHONE: {
            "name": "phone",
            "type": "str",
        },
        FILD_NAME: {
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

    def check_name(self, fild_name: str) -> None:
        """Próba przypisania niewłaściwej wartości do atrybutu wywoła błąd."""
        if fild_name in self._FILDS_CONFIGURATION:
            self._name = fild_name
        else:
            raise ValueError(f"{fild_name} is an invalid value for name")

    def get_field_configuration(self) -> dict:
        return self._FILDS_CONFIGURATION.get(self.name)

    def __repr__(self):
        return f"Fild('{self._name}')"
