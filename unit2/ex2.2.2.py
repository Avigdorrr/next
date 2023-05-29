class Fox:
    def __init__(self):
        self.name = ""
        self.age = 0

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    fox1 = Fox()
    fox2 = Fox()
    fox1.birthday()
    print(fox1.get_age())
    print(fox2.get_age())


if __name__ == '__main__':
    main()