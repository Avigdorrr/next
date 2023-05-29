class BigThing:

    def __init__(self, var):
        self._var = var

    def size(self):
        if isinstance(self._var, int):
            return self._var
        if isinstance(self._var, (str, dict, list)):
            return len(self._var)


class BigCat(BigThing):

    def __init__(self, name, var):
        self._name = name
        super().__init__(var)

    def size(self):
        if super().size() > 20:
            return "Very Fat"
        if super().size() > 15:
            return "Fat"



def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()