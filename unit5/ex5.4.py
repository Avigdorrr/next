class IDIterator:
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


def check_id_valid(id_number):
    digits = (int(digit) for digit in str(id_number))
    multiplied_digits = (digit * 2 if idx % 2 == 0 else digit for idx, digit in enumerate(digits, start=1))
    summed_digits = (digit if digit < 10 else sum(map(int, str(digit))) for digit in multiplied_digits)
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0

def id_generator(id_number):
    for num in range(id_number, 999999999 + 1):
        if check_id_valid(num):
            yield num


def main():
    my_id = int(input("enter id: "))
    choose = input("""enter : "it" for iterator or "gen" for generator""")

    if choose == "it":
        id_iter = iter(IDIterator(my_id))
        for i in range(10):
            print(next(id_iter))
    elif choose == "gen":
        my_id = int(input("enter id: "))
        id_gen = id_generator(my_id)
        for i in range(10):
            print(next(id_gen))
    else:
        print("u idiot <3")


if __name__ == '__main__':
    main()