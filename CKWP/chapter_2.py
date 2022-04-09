# Kod Pythoniczny

## Wyrażenia składowe i wyrażenia przypisania


def run_calculations(i: int) -> int:
    return i + 5


numbers = []
for i in range(10):
    numbers.append(run_calculations(i))

numbers = [run_calculations(i) for i in range(10)]


# Znaki podkreślenia w Pythonie
class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60
