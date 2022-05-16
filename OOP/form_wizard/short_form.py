from typing import List
from fild import Fild


class ShortForm:
    _name = "short-form"
    _filds = [
        Fild(Fild.FILD_NAME),
        Fild(Fild.FILD_PHONE),
    ]

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_filds(self) -> list:
        """Zwraca listę obiektów Fild"""
        return self._filds

    def get_field_configuration(self) -> List[dict]:
        """Tworzy listę, która zawiera dickta dostępnych pól wraz z konfiguracją"""
        list_field_configuration = []
        for fild in self.get_filds:
            list_field_configuration.append(fild.get_field_configuration())
        return list_field_configuration

    def __repr__(self):
        return f"ShortForm('{self._name}', {self._filds})"
