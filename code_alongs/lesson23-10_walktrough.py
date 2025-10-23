from numbers import Number

class UnitConverter:
    def __init__(self, value: int | float): #| means or
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, Number):
            raise TypeError ('input a value that is a number')
        if not value >= 0:
            raise ValueError ('number should be larger or equal to 0')
        self._value = value
    

unit_converter = UnitConverter(3)

print(f'{unit_converter.value = }')
