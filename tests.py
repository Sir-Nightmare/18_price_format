import unittest
from format_price import format_price


class PriceFormatTestCase(unittest.TestCase):
    def test_big_int_value(self):
        self.assertEqual(format_price(9876543210), '9 876 543 210')

    def test_float_value(self):
        self.assertEqual(format_price(9876.54), '9 876.54')

    def test_float_with_zeros(self):
        self.assertEqual(format_price(54321.00), '54 321')

    def test_int_string(self):
        self.assertEqual(format_price('109876543210'), '109 876 543 210')

    def test_float_string_dot(self):
        self.assertEqual(format_price('12345.67'), '12 345.67')

    def test_float_string_comma(self):
        self.assertEqual(format_price('12345,67'), '12 345.67')

    def test_incorrect_string(self):
        with self.assertRaises(ValueError):
            format_price('qwert1234')

    def test_incorrect_list(self):
        with self.assertRaises(ValueError):
            format_price(['123456'])


if __name__ == '__main__':
    unittest.main()
