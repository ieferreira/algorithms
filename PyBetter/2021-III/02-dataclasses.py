"""
Classes are a combination of behavior and data (methods and attributes)

A class sometimes behaves as a data container.

Data oriented variant of a class (in csharp it's called a struct)
Data Class: quick initializer

"""
from dataclasses import dataclass, field


class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


person1 = Person("Iván", "Programmer", "24")
person2 = Person("Eduardo", "Geologist", "25")
person3 = Person("Eduardo", "Geologist", "25")


print(id(person2))
print(id(person3))
print(person1)

# are different even though they contain the same information
print(person3 == person2)


# using a dataclass
print("--- USING A DATACLASS ---")


@dataclass(order=True, frozen=True)  # frozen is read only
class Persona:
    # not part of the string rep
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100
    # define that can be ordered

    def __post_init__(self):
        # self.sort_index = self.age  # sort by age
        # self.sort_index = self.strength # sort by strength
        # circumvent frozen attribute
        object.__setattr__(self, "sort_index", self.strength)

    def __str__(self):
        return f"Character: {self.name}, {self.age} years old and he is a {self.job} of {self.strength} Strength"


person1 = Persona("Iván", "Programmer", 24, 99)
# person1.age = 25  error because it is frozen
person2 = Persona("Eduardo", "Geologist", 25)
person3 = Persona("Eduardo", "Geologist", 25)


print(id(person2))
print(id(person3))
print(person1)

# are different even though they contain the same information
print(person3 == person2)
print(person2 > person1)
