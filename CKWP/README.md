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