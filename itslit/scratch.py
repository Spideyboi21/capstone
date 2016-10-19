class Person:
    def __init__(self, name):
        self.name = Name(name)


class Name:
    def __init__(self, name):
        self.name = name

chris = Person('Chris')

print(chris.name.name)
