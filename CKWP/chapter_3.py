# from contracts import contract
#
#
# @contract(a=int, b='int,>0')
# def my_sum(a, b):
#     return a + b
#
#
# my_sum("text", 1)
# my_sum(1, 0)

# Zmienna liczba argumentów
l = [1, 2, 3]


def f(*list_num: list):
    for num in list_num:
        print(num)


f(l)


def show(e, rest):
    print("Element: {0} - Reszta: {1}".format(e, rest))


first, *rest = [1, 2, 3, 4, 5]
show(first, rest)

first, *middle, last = range(6)


def show_dict(**kwargs):
    print(kwargs)


def last_show_dict(name="Nieznany", **kwargs):
    print(name)
    print(kwargs)


show_dict(name="Tomas", lastname="Strach", city="Warsaw")
last_show_dict(name="Tomas", lastname="Strach", city="Warsaw")
