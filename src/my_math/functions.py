""" Math fuctions """

def factorial(number: int) -> int:
    if number == 1:
        return 1
    return factorial(number - 1) * number
