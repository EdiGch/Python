from typing import List
from field import Field


class ShortForm:
    _name = "short-form"
    _fields = [
        Field(Field.FIELD_NAME),
        Field(Field.FIELD_PHONE),
    ]

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_filds(self) -> list:
        """Zwraca listę obiektów Fild"""
        return self._fields

    def get_fields_configuration(self) -> List[dict]:
        """Tworzy listę, która zawiera dickta dostępnych pól wraz z konfiguracją"""
        list_field_configuration = []
        for field in self.get_filds:
            list_field_configuration.append(field.get_field_configuration())
        return list_field_configuration

    def __repr__(self):
        return f"ShortForm('{self._name}', {self._fields})"
