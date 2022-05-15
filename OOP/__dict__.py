from typing import List


class TypeForms:
    """Klasa odpowiada za przechowywanie danych o formularzu
    :param variant: Atrybut opisuje warianty formularzy
    """

    type_forms: List[str] = [
        'short-form',
        'data-collector'
    ]

    def __init__(self, variant: str):
        self.variant = variant


type_forms = TypeForms("Poland")

print(type_forms.__dict__)
print(help(type_forms))
