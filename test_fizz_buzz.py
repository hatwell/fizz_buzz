import unittest

from fizz_buzz import fizz_buzz, translate_number


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(True, True)

    def test_prints_zero_if_given_no_argument(self):
        result = fizz_buzz()
        self.assertEqual(result, 0)


class TestTranslateNumber(unittest.TestCase):
    def test_one_returns_one(self):
        result = translate_number(1)
        self.assertEqual(result, 1)

    def test_multiple_of_three_returns_fizz(self):
        result = translate_number(3)
        self.assertEqual(result, 'Fizz')

    def test_multiple_of_five_returns_buzz(self):
        result = translate_number(5)
        self.assertEqual(result, 'Buzz')

    def test_multiple_of_seven_returns_baz(self):
        result = translate_number(7)
        self.assertEqual(result, 'Baz')


if __name__ == "__main__":
    unittest.main()
