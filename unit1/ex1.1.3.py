def four_dividers(number):
    return list(filter(four_dividers_helper, range(1, number+1)))


def four_dividers_helper(number):
    return number % 4 == 0
