from numbers import Number
from utils import validate_positive_number

class UnitConverter:
    def __init__(self, value: Number): #| means or
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        validate_positive_number(value)

        self._value = value

    def inch_to_cm(self):
        return 2.54 * self.value
    

unit_converter = UnitConverter(5)

print(f'{unit_converter.value = }')
print(unit_converter.inch_to_cm())
