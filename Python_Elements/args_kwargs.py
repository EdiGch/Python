args = [1, 3, 6]
kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}


def func1(*args):
    print(*args)
    print(type(args))
    print(args)
    print(type(args))


func1(args)


def func2(agr1, agr2, agr3):
    print(agr1, agr2, agr3)


func2(*args)

print("=============================\n")


def func3(*kwargs):
    print(*kwargs)
    print(type(kwargs))
    print(kwargs)
    print(type(kwargs))


func3(kwargs)


def func4(agr1, agr2, agr3):
    print(agr1, agr2, agr3)


func4(*kwargs)
