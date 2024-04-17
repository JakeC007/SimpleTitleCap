"""
Unit testing the cap
4/17/24
J. Chanenson
"""
import unittest
from simpcap import convert_to_title_case

class TestTitleCaseConversion(unittest.TestCase):

    def test_basic_title_case(self):
        input_text = "hello world"
        expected_output = "Hello World"
        self.assertEqual(convert_to_title_case(input_text), expected_output)

    def test_title_case_with_punctuation(self):
        input_text = "hello, world! how are you?"
        expected_output = "Hello, World! How Are You?"
        self.assertEqual(convert_to_title_case(input_text), expected_output)

    def test_title_case_with_special_words(self):
        input_text = "the lion, the witch, and the wardrobe"
        expected_output = "The Lion, the Witch, and the Wardrobe"
        self.assertEqual(convert_to_title_case(input_text), expected_output)

    def test_title_case_with_special_cases(self):
        input_text = "mr. smith goes to washington"
        expected_output = "Mr. Smith Goes to Washington"
        self.assertEqual(convert_to_title_case(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
