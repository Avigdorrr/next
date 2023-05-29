class Fox:
    count_animals = 0

    def __init__(self, name="Bob"):
        self._name = name
        self._age = 0
        Fox.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1


def main():
    fox1 = Fox("Moshe")
    fox2 = Fox()
    print(fox1.get_name())
    print(fox2.get_name())
    fox1.set_name("Roy")
    print(fox1.get_name())
    print(Fox.count_animals)
