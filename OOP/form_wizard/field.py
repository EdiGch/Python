from typing import Final


class Field:
    FIELD_PHONE: Final[str] = "phone"
    FIELD_NAME: Final[str] = "name"
    _FIELDS_CONFIGURATION: Final[dict] = {
        FIELD_PHONE: {
            "name": "phone",
            "type": "str",
        },
        FIELD_NAME: {
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

    def check_name(self, field_name: str) -> None:
        """Próba przypisania niewłaściwej wartości do atrybutu wywoła błąd."""
        if field_name in self._FIELDS_CONFIGURATION:
            self._name = field_name
        else:
            raise ValueError(f"{field_name} is an invalid value for name")

    def get_field_configuration(self) -> dict:
        return self._FIELDS_CONFIGURATION.get(self.name)

    def __repr__(self):
        return f"Fild('{self._name}')"
