import unittest

from fizz_buzz import fizz_buzz, get_modulii


class TestFizzBuzz(unittest.TestCase):
    def test_three_returns_fizz(self):
        result = fizz_buzz(3)
        self.assertEqual(result, 'Fizz')

    # def test_five_returns_buzz(self):
    #     result = fizz_buzz(5)
    #     self.assertEqual(result, 'Buzz')
    
#     def test_seven_returns_baz(self):
#         result = fizz_buzz(7)
#         self.assertEqual(result, 'Baz')

#     def test_multiple_of_three_returns_fizz(self):
#         result = fizz_buzz(6)
#         self.assertEqual(result, 'Fizz')

#     def test_multiple_of_five_returns_buzz(self):
#         result = fizz_buzz(10)
#         self.assertEqual(result, 'Buzz')
    
#     def test_multiple_of_seven_returns_baz(self):
#         result = fizz_buzz(14)
#         self.assertEqual(result, 'Baz')

#     def test_other_returns_self(self):
#         result = fizz_buzz(1)
#         print(result, ">>>>>")
#         self.assertEqual(result, '1')
    
#     def test_other_returns_self(self):
#         result = fizz_buzz(11)
#         print(result, ">>>>>")
#         self.assertEqual(result, '11')


class TestGetModuli(unittest.TestCase):
    
    def test_three_returns_two_zeroes(self):
        self.assertEqual(get_modulii(3), [0, 3, 3])

    def test_five_returns_one_zero(self):
        self.assertEqual(get_modulii(5), [2, 0, 5])

    



if __name__ == "__main__":
    unittest.main()
