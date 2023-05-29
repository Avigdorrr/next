FILE_NAME = "unit1/names.txt"


def ex1():
    with open(FILE_NAME, 'r') as input_file:
        return max(input_file.read().split("\n"), key=len)


def ex2():
    with open(FILE_NAME, 'r') as input_file:
        return sum(len(name) for name in input_file.read().split("\n"))


def ex3():
    with open(FILE_NAME, 'r') as input_file:
        data = input_file.read().split("\n")
    min_name = min(data, key=len)
    return "\n".join(filter(lambda name: len(name) == len(min_name), data))


def ex4():
    with open(FILE_NAME, 'r') as input_read:
        with open(r'unit1/name_length.txt', 'w') as input_write:
            input_write.write("\n".join(map(lambda name: str(len(name)), input_read.read().split("\n"))))


def ex5():
    length = int(input("enter length"))
    with open(FILE_NAME, 'r') as input_file:
        return "\n".join(filter(lambda name: len(name) == length, input_file.read().split("\n")))