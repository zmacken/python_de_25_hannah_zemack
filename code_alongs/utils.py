from numbers import Number

def validate_positive_number(value) -> None:
    if not isinstance(value, Number):
        raise TypeError ('input a value that is a number')
    if not value >= 0:
        raise ValueError ('number should be larger or equal to 0')