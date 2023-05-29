def is_prime(number):
    return False not in [True if number % n != 0 else False for n in range(2, number)]