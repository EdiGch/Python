# ENV KONFIGURACJA
Chcąc uniknąć instalacji w przestrzeni globalnej należy użyć wirtualnego
środowiska. W przypadku, gdy mamy kilka projektów i te potrzebują do działania różnych wersji tej samej biblioteki mamy
problem. Rozwiązaniem jest użycie biblioteki virtualenv. Pozwala ona na tworzenie odizolowanych środowisk z Pythonem i
zależnościami.

* Stworzenie środowiska wirtualnego env. 
    * Aby zainstalować virtualenv wpisujemy w konsoli:
      ```shell
        pip install virtualenv
      ```
    * Instalacja virtualenv w katalogu projektu:
      ```shell
      virtualenv -p python3.10 env
      ```
    * Wejście/uruchomienie środowiska wirtualnego:
      ```shell
      source env/bin/activate
      ```
    * Wyjście/dezaktywacja środowiska wirtualnego:
      ```shell
      deactivate
      ```

Tworząc projekt warto podać w pliku requirements.txt listę zależności, które są wymagane by uruchomić projekt.
* Instalacja zależności z pliku
    * Wejście/uruchomienie środowiska wirtualnego:
      ```shell
      source env/bin/activate
      ```
    * Instalacja z pliku:
      ```shell
      pip install -r requirements.txt
      ```
      
Menadżer pakietów pip. Lista podstawowych komend:
 ```shell
pip install <package>           # instalacja pakietu
pip install <package> --upgrade # aktualizacja pakietu
pip uninstall                   # odinstalowuje pakiety
pip list                        # wyświetla listę zainstalowanych pakietów
pip list --outdated             # wyświetla listę nieaktualnych pakietów
pip show                        # wyświetla szczegóły na temat pakietu
pip freeze                      # wyświetla listę zainstalowanych pakietów w formacie plików requirements.txt
pip freeze > requirements.txt   # Zapisuje w pliku listę zainstalowanych pakietów
pip install -r requirements.txt # instaluje zależności z pliku requirements.txt
```

## Pipenv Wprowadzenie

* Instalacja
```shell
pip install pipenv
```

* Wejście do powłoki w środowisku wirtualnym, aby odizolować rozwój aplikacji.
Stworzy to środowisko wirtualne, jeśli jeszcze nie istnieje. Pipenv tworzy wszystkie twoje 
wirtualne środowiska w domyślnej lokalizacji. 
```shell
pipenv shell
```

* Instalacja paketu
```shell
pipenv install djangorestframework
```