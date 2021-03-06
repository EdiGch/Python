from copy import copy


class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        """Information more dev/code user oriented"""
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    def __str__(self):
        """Information user"""
        return f"{self.title} by {self.author} on {self.book_type}"

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.author}"

        return repr(self)


b = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
# print(str(b))
# print(b)
# print(b.__dict__)

print(repr(b))
print(eval(repr(b)))
print(f"{b:short}")


class Book:
    """
    Object Equality
    """

    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        """Information more dev/code user oriented"""
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False

        return self.title == other.title and self.author == other.author


a = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
z = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)

print(a == z)

print(id(a))
print(id(z))


# Mutowalne struktury danych

class Tire:
    def __init__(self, kind, distance_covered):
        self.kind = kind
        self.distance_covered = distance_covered


class BMW:
    doors = 2
    model = "E46"
    wheels = 4
    tires = [Tire("operational", 10) for i in range(4)]

    def __init__(self, color="black"):
        self.color = color


bmw1 = BMW()
print(bmw1.tires)  # 4 różne instancje Tire
for tire in bmw1.tires:
    """Funkcja id() Pythona zwraca „tożsamość” obiektu. Tożsamość obiektu jest liczbą całkowitą, 
    która gwarantuje, że jest unikalna i stała dla tego obiektu podczas jego życia."""
    print(id(tire))
bmw2 = BMW()
print(bmw2.tires)  # 4 różne instancje Tire
for tire2 in bmw2.tires:
    """Funkcja id() Pythona zwraca „tożsamość” obiektu. Tożsamość obiektu jest liczbą całkowitą, 
    która gwarantuje, że jest unikalna i stała dla tego obiektu podczas jego życia."""
    print(id(tire2))  # Te samo id jak w instancji bmw1 !

print("===================================================================\n")
print("=================== DODANIE OBIEKTU DO LISTY ======================\n")
print("================================ BMW1 ================================\n")
# Dodajmy kolejną oponę do instancji bmw1
bmw1.tires.append(Tire(kind="spare", distance_covered=1000))
for tire in bmw1.tires:
    print(id(tire))

print("================================ BMW2 ================================\n")

for tire2 in bmw2.tires:
    print(
        id(tire2))  # Pomimo dodania do instanji bmw1 nowego objektu, on również jest dostępny w bmw2


# Hashable Book
class Book:
    """
    Object Equality
    """

    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        """Information more dev/code user oriented"""
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False

        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.pages > other.pages

    def __lt__(self, other):
        return NotImplemented

    def __len__(self):
        return NotImplemented

    def __ge__(self, other):
        return NotImplemented

    def __hash__(self):
        return hash((self.title, self.author))


a = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
z = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)

print(a == z)

print(id(a))
print(id(z))
print(hash(z))
print(hash(z))

from functools import total_ordering


@total_ordering
class Book:
    """
    Object Equality
    """

    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        """Information more dev/code user oriented"""
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False

        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.pages > other.pages

    def __hash__(self):
        return hash((self.title, self.author))


# Book = total_ordering(Book) or add @total_ordering
a = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
z = Book("How Asia", "Nassim Taleb", "Hardcover", 472)

print(a == z)
print(a != z)
print(a < z)
print(a <= z)
print(a > z)
print(a >= z)


class Warehouse:
    def __init__(self):
        self.rack = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only isinstance Book could be added to the Book")

        self.rack.append(book)

    def __add__(self, other):
        if not isinstance(other, Book):
            raise TypeError("__add__ Only isinstance Book could be added to the Book")

        new_werehouse = Warehouse()

        for book in self.rack:
            new_werehouse.add_book(book)

        new_werehouse.add_book(other)

        return new_werehouse

    def __getitem__(self, item):
        return self.rack[item]


warehouse = Warehouse()
a = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
z = Book("How Asia", "Nassim Taleb", "Hardcover", 472)

warehouse.add_book(a)
warehouse.add_book(z)

print(warehouse.__dict__)
print(warehouse[0])
