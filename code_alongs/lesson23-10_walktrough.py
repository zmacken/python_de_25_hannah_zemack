from numbers import Number
from utils import validate_positive_number

class UnitConverter:
    def __init__(self, value: int | float): #| means or
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        validate_positive_number(value)

        self._value = value
    

unit_converter = UnitConverter(5)

print(f'{unit_converter.value = }')
