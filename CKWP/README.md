# Czysty kod w Pythonie
Twórz wydainy i łatwy w utrzymaniu kod

## Docstring
sphinx.ext.autodoc – Include documentation from docstrings
https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

## Adnotacje
```shell
def process_clients(clients: list[tuple[int, str]]):
```

## Sprawdzenie spójności typów
Mypy to opcjonalny moduł sprawdzania typów statycznych dla Pythona.ls
http://www.mypy-lang.org/
Uruchamianie:
```shell
mypy <nazwa pliku>
mypy CKWP/chapter_1.py
```
Pytype sprawdza i wnioskuje typy dla twojego kodu Pythona — bez konieczności adnotacji typu.
https://google.github.io/pytype/

## Ogólne spawdzenie poprawności w kodzie
Pylint to narzędzie, które sprawdza błędy w kodzie Pythona, próbuje wymusić standard kodowania.
https://pylint.pycqa.org/en/latest/intro.html

```shell
pylint CKWP/chapter_1.py
```

## Formatowanie automatyczne 
1. flake8
2. black (https://github.com/psf/black)

# Kod Pythoniczny

## Menadzer Kontekstów
Menadżer kontekstu (ang. context manager) to obiekt, który odpowiednio zarządza danym zasobem, 
zapewniając, że zostanie on odpowiednio zamknięty. Przez zamknięty mam tu na myśli czyszczenie, 
zwalnianie zasobów oraz sprzątanie po wykonaniu bloku kodu.
```shell
with open("text.txt") as file:
    lines = file.readlines()
    print(lines)
```

## Wyrażenia składowe i wyrażenia przypisania 
Wyrażenia składane zaleca się stosować w celu tworzenia struktór danych za pomocą pojedynczej 
instrukcji, zamiast z wykorzystaniem wielu instrukcji. Aby na przykład utworzyć listę zawierającą 
wyniki obliczeń na liczbach
```shell
numbers = []
for i in range(10):
  numbers.append(run_calculayion(i))
  
numbers = [run_calculayion(i) for i in range(10)]
```

## Właściwości, atrybuty i różne typy metod obiektów
Wszystkie właściwości i funkcje objektu w jezyku Python (3.10) są publiczne. 
Nie istnieje mechanizm ścisłego egzekwowania ale istnieje pewne konwencje. Atrybut zaczynający się 
od podkreślenia ma być prywatny.
```shell
class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60
```