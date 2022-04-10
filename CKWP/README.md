# Czysty kod w Pythonie
Czysty kod w Pythonie. Twórz wydajny i łatwy w utrzymaniu kod. Wydanie II.
Autor: Mariano Anaya 
Data wydania książki drukowanej: 2022-03-22

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

## Właściwości 
* Nie pisz niestandardowych metod get_* i set_* dla wszystkich atrybótów obiektów. W wiekszoście 
przypadków wystarczy pozostawić je jako zwykłe atrybuty. Jeśli chcesz zmodyfikować logikę podczas 
pobierania lub modyfikowania atrybutu, użyj własciwości.
* Zasada separacji mówi, że metoda obiektu powinna albo odpowiadać na coś albo coś robić, 
ale nie jedno i drugie. Fukcje powinny robić jedną rzecz i tylko jedną rzecz. 
```shell
@property
@longitude.setter
```

## Tworzenie klas o bardziej zwartej składni (@dataclass)
* Dataclass pozwala na definiowanie klas z mniejszą ilością kodu i większą funkcjonalnością po 
wyjęciu z pudełka.
* Dekorator dataclass daje dostęp do:
  * eprezentację obiektu w postaci ciągu, podczas printowania obiektu, otrzymasz czytelny format
  * porównać dwie instancje klasy według atrybutu
* Dekorator @dataclass niejawnie tworzy __init__
* Wartości domyślne, Podobnie jak w przypadku reguł dotyczących parametrów, atrybuty z wartościami 
domyślnymi muszą pojawić się po atrybutach bez wartości domyślnych.
* Konwertuj na krotkę lub słownik, moduł dataclasses posiada funkcje astuple()i asdict(), 
które konwertują instancję dataclass na krotkę i słownik: print(astuple(p)), print(asdict(p))
* Służy frozen=Truedo definiowania klasy, której obiekty są niezmienne.
* Użyj __post_init__metody, aby zainicjować atrybuty zależne od innych atrybutów.
* Służy sort_indexdo określania atrybutów sortowania obiektów klasy danych.

```shell
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    
p1 = Person('John', 25)
p2 = Person('John', 25)
print(p1 == p2)
    
print(astuple(p))
print(asdict(p))
```