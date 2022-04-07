from typing import Tuple
from dataclasses import dataclass


## Docstring
def my_function():
    """Uruchom jakieś obliczenia"""
    return None


var = my_function.__doc__  # help(my_function)
print(var)

## Adnotacje

Seconds = float


def launch_task(delay: Seconds):
    return None


Client = Tuple[int, str]


def process_clients(clients: list[tuple[int, str]], last_clients: list[Client]):
    for client in clients:
        print(client)

    for last_client in last_clients:
        print(last_client)

    return None


my_clients = [
    (10, 'top'),
    (10, 'tom'),
]
my_last_clients = [
    (10, 'top'),
    (10, 'top'),
]
process_clients(my_clients, my_last_clients)


@dataclass
class Point:
    lat: float
    long: float


print(Point.__annotations__)

## Sprawdzenie spójności typów
