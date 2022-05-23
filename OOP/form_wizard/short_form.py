from typing import List
from field import Field


class ShortForm:
    _name: str = "short-form"
    _fields: List[Field] = [
        Field(Field.FIELD_NAME),
        Field(Field.FIELD_PHONE),
    ]

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_fields(self) -> List[Field]:
        """Zwraca listę obiektów Fild"""
        return self._fields

    def get_fields_configuration(self) -> List[dict]:
        """Tworzy listę, która zawiera dickta dostępnych pól wraz z konfiguracją"""
        return [field.get_field_configuration() for field in self.get_fields]

    def __repr__(self):
        return f"ShortForm('{self._name}', {self._fields})"
