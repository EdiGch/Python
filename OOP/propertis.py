class Customer:
    _loyalty_levels: set = {"bronze", "gold", "platinum"}

    def __init__(self, loyalty):
        self.set_loyalty(loyalty)

    def get_loyalty(self):
        return self.__loyalty

    def set_loyalty(self, level):
        if level not in type(self)._loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")

        self.__loyalty = level


c = Customer("bronze")
c.__loyalty = "custom"  # obejście
print(c.__loyalty)
print(c.__dict__)

c = Customer("bronze")
print(c._Customer__loyalty)  # safety, not restriction access
print(c.__loyalty)  # AttributeError
print(c.__dict__)
