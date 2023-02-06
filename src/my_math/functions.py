""" Math fuctions """


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError('Number cannot be negative')
    if number == 0 or number == 1:
        return 1
    return factorial(number - 1) * number
