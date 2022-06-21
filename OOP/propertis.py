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
# print(c.__loyalty)  # AttributeError
print(c.__dict__)


class CustomerV2:
    _loyalty_levels: set = {"bronze", "gold", "platinum"}

    def __init__(self, loyalty, membership=0):
        self.loyalty = loyalty
        self.membership = membership

    def get_membership(self):
        return self._membership

    def set_membership(self, value):
        if value < 0 or value > 34:
            raise ValueError(f"Invalid membership years")

        self._membership = value

    def get_loyalty(self):
        return self._loyalty

    def set_loyalty(self, level):
        if level not in type(self)._loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")

        self._loyalty = level

    loyalty = property(fget=get_loyalty, fset=set_loyalty)
    membership = property(fget=get_membership, fset=set_membership)


# c = CustomerV2("bronze", 120)
c = CustomerV2("bronze", 12)