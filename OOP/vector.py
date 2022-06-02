import math
from math import hypot
from functools import total_ordering


@total_ordering
# Vector is a class that represents a vector in a two-dimensional space.
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """
        "If the other object is not a Vector, raise a TypeError, otherwise return a new Vector with
        the sum of the x, y, and z values of the two vectors."

        The first line of the function checks to see if the other object is a Vector. If it is not,
        then the function raises a TypeError. If it is, then the function returns a new Vector with
        the sum of the x, y, and z values of the two vectors

        :param other: The other vector to add to this one
        :return: A new instance of Vector
        """
        if not isinstance(other, Vector):
            raise TypeError("Operation only supported between instances of vectors")

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        """
        "If the other object is not a number, raise an error. Otherwise, return a new Vector object
        with the coordinates multiplied by the other object."

        The __mul__ function is called when the * operator is used on a Vector object

        :param other: The other object that is being multiplied with the current object
        :return: A new Vector object with the same direction as the original, but with a magnitude
        that is the product of the original magnitude and the scalar.
        """
        if not type(other) == int and not type(other) == float:
            raise TypeError("Operation only supported for a numeric scalar")

        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        # return math.hypot(self.x, self.y, self.z)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __le__(self, other):
        """
        If the other object is not a vector, return a TypeError. Otherwise, return the result of the
        comparison of the absolute value of self and the absolute value of other.

        :param other: The other vector to compare to
        :return: The magnitude of the vector
        """
        if not isinstance(other, Vector):
            return TypeError("Must be a vector")

        return abs(self) < abs(other)

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")
        else:
            return NotImplemented


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 6)
    v3 = Vector(0, 0, 0)

    print(bool(v1))
    print(bool(v3))
    print(v1)  # Vector(1, 2, 3)
    print(v2)  # Vector(2, 3, 6)
    print(v1 + v2)  # Vector(3, 5, 9)
    print(v1 * 2)  # Vector(2, 4, 6)
    print(v1 < v2)  # True
    print(v1.z)  # 3
    print(v1['Z'])  # 3
    print(v1['Zero'])  # NotImplemented
