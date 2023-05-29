import functools


def sum_of_digits(number):
    return int(functools.reduce(sum_of_digits_helper, list(str(number))))


def sum_of_digits_helper(num1, num2):
    return int(num1) + int(num2)
