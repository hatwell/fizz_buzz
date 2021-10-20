import unittest 
from kwic import Kwic


class TestKwic(unittest.TestCase):
    def test_returns_list_of_substrings_of_supplied_length(self):
        self.assertEqual(Kwic('the cat sat on the mat', 3).get_output(), ["the cat sat","sat on the","cat sat on","on the mat"])

    def  test_works_with_two_words(self):
        result = Kwic("I love bears", 2).get_output()
        self.assertEqual(result, [ "love bears", "I love"])







if __name__ == "__main__":
    unittest.main()        