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
        """Zwraca stringa z nazwami dostępnych formularzy oddzielone przecinkami"""
        list_available_forms = []
        for form in self.get_forms_types:
            list_available_forms.append(form.get_name)

        return ", ".join([str(x) for x in list_available_forms])

    def get_available_field(self) -> dict[str, list]:
        """Tworzy dicta, który zawiera nazwę formularza a w nim listę dostępnych pól"""
        dict_field_configuration = {}
        for form in self.get_forms_types:
            dict_field_configuration[form.get_name] = form.get_fields_configuration()

        return dict_field_configuration

    def get_field_configuration(self, name_type_form: str) -> dict:
        """Pobiera konfigurację formularza na podstawie jego nazwy
        :param name_type_form: nazwa formularza (str)
        """
        dict_field_configuration = {}
        if name_type_form in self.get_available_forms():
            for form in self.get_forms_types:
                if form.get_name == name_type_form:
                    dict_field_configuration[form.get_name] = form.get_fields_configuration()

                    return dict_field_configuration

        else:
            raise ValueError(f"{name_type_form} is an invalid value for name")

    def __repr__(self):
        return f"FormsTypes('{self._forms_types}')"
