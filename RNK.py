import unittest


class RomanNumeralConverter(object):
    def convert(self, number):
        roman_numeral = ""

        if (number >= (10 - 1)):
            if (number < 10):
                roman_numeral = "I"
                number = number + 1
            roman_numeral = roman_numeral + "X"
            number = number - 10

        if (number >= (5 - 1)):
            if (number < 5):
                roman_numeral = roman_numeral + "I"
                number = number + 1
            roman_numeral = roman_numeral + "V"
            number = number - 5

        roman_numeral = roman_numeral + (number * "I")

        return roman_numeral


class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.my_converter = RomanNumeralConverter()

    def test_converts_one(self):
        self.assertEquals(self.my_converter.convert(1), "I")

    def test_converts_two(self):
        self.assertEquals(self.my_converter.convert(2), "II")

    def test_converts_five(self):
        self.assertEquals(self.my_converter.convert(5), "V")

    def test_converts_six(self):
        self.assertEquals(self.my_converter.convert(6), "VI")

    def test_converts_four(self):
        self.assertEquals(self.my_converter.convert(4), "IV")

    def test_converts_ten(self):
        self.assertEquals(self.my_converter.convert(10), "X")

    def test_converts_nine(self):
        self.assertEquals(self.my_converter.convert(9), "IX")


if __name__ == '__main__':
    unittest.main()
