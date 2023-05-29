def first_prime_over(n):
    x = (x for x in range(n + 1, n*n) if is_prime(x))
    return next(x)

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True