cities = ['San Francisco', 'New York', 'Washington DC']
print(len(cities))

# Sprawdzanie, czy element istnieje w sekwencji Pythona
print('New York' in cities)

# Aby zanegować inoperator, użyj notoperatora. Poniższy przykład sprawdza,
# czy 'New York'nie ma go na citiesliście
print('New York' not in cities)

# Znajdowanie indeksu elementu w sekwencji Pythona
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5))

# Poniższy przykład zwraca indeks pierwszego wystąpienia liczby 5 po trzecim indeksie:
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5, 3))

# Krojenie sekwencji
# Aby pobrać wycinek z indeksu ido (ale nie w tym) j, użyj następującej składni:
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers[2:6])
print(numbers[::2])
print(numbers[2::])

print(max(numbers))
print(min(numbers))

# Łączenie dwóch sekwencji Pythona
# Aby połączyć dwie sekwencje w jedną sekwencję, użyj operatora +
east = ['New York', 'New Jersey']
west = ['San Diego', 'San Francisco']

cities = east + west
print(cities)

# Łączenie sekwencji niezmiennych jest całkiem bezpieczne. Poniższy przykład dołącza jeden
# element do listy zachodniej. I nie wpływa to na kolejność miast:
west.append('Sacramento')
print(west)
print(cities)