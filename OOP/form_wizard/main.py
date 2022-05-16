from forms_types import FormsTypes

class Validate:

    def validate_type(self, value):
        forms_types_obj = FormsTypes()

        forms_list = forms_types_obj.get_available_field()

        if value in forms_types_obj.get_available_forms():
            return value
        else:
            raise FileNotFoundError(
                f"The specified form type does not exist. "
                f"You can use the following types: {forms_types_obj.get_available_forms_str()}")


if __name__ == "__main__":
    validate = Validate()

    list_forms = [
        'short-form',
        'press-form',
    ]

    for list_form in list_forms:
        print(validate.validate_type(list_form))