class UnitConverter:
    def __init__(self, value: int | float): #| means or
        self.value = value

unit_converter = UnitConverter(5)

print(f'{unit_converter.value = }')
