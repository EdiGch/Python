from typing import List
import random


class Student:
    education_platform: str = "Udemy"

    def __init__(self, name: str, age: int = 34):
        self.name = name
        self.age = age

    def greet(self) -> str:
        _greetings = [
            "Hi, I'm {}",
            "hey there, my name is {}",
            "Hi, oh, my name is {}"
        ]

        greeting: str = random.choice(_greetings)

        return greeting.format(self.name)


def class_create(student_names: List[str]):
    for name in student_names:
        student = Student(name)
        print(student.greet())


if __name__ == "__main__":
    names = ["Alice", "Brian", "Anna", "Greg"]

    class_create(names)
