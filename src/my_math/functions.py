""" Math fuctions """


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError('Number cannot be negative')
    if number == 0 or number == 1:
        return 1
    return factorial(number - 1) * number


def power_positive(base: int, pwr: int) -> int:
    if pwr == 0:
        return 1
    return power_positive(base, pwr - 1) * base


def power_negative(base: int, pwr: int) -> int:
    if pwr == 0:
        return 1
    return power_negative(base, pwr + 1) / base


def power(base: int, pwr: int) -> int:
    if pwr == 0:
        return 1
    if pwr > 0:
        return power_positive(base, pwr)
    return power_negative(base, pwr)
