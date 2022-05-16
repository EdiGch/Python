from typing import List
from short_form import ShortForm


class FormsTypes:
    _forms_types = [
        ShortForm(),
    ]

    @property
    def get_forms_types(self) -> list:
        return self._forms_types

    def get_available_forms(self) -> List[str]:
        """Zwraca listę nazw dostępnych formularzy"""
        list_available_forms = []
        for form in self.get_forms_types:
            list_available_forms.append(form.get_name)

        return list_available_forms

    def get_available_forms_str(self) -> str:
        """Zwraca stringa nazw dostępnych formularzy"""
        list_available_forms = []
        for form in self.get_forms_types:
            list_available_forms.append(form.get_name)

        return ", ".join([str(x) for x in list_available_forms])

    def get_available_field(self) -> dict[str, list]:
        """Tworzy dicta, który zawiera nazwę formularza a w nim listę dostępnych pól"""
        dict_field_configuration = {}
        for form in self.get_forms_types:
            dict_field_configuration[form.get_name] = form.get_field_configuration()

        return dict_field_configuration

    def __repr__(self):
        return f"FormsTypes('{self._forms_types}')"
