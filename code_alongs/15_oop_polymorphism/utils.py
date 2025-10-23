from numbers import Number

def validate_number(value):
    if not isinstance(value, Number):
        raise TypeError (f'value must be numbers, not {type(value)}')