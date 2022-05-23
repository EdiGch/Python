class BaseResponse:
    _errors: list = []

    def __init__(self, errors):
        self._errors.append(errors)

    def get_prepared_message(self) -> dict:
        return {
            "message": "Something went wrong",
            "errors": self._errors
        }