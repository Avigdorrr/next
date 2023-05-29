def get_fibo():
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while True:
        yield num1 + num2
        num1, num2 = num2, num1 + num2