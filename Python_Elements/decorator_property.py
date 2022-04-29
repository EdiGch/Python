def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()

    return new_function


@decorator
def initial_function():
    print("Initial Functionality")


initial_function()


class House:

    def __init__(self, price):
        self._price = price

    @property  # Getter
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


house = House(50000.0)
print(house.price)
house.price = 4000.00
print(house.price)
