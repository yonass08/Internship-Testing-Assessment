import unittest
from string_functions import *


class TestToUpper(unittest.TestCase):
    # write your code here
    def test_to_upper_type(self):
        # check that to_upper fails when the input is not a string
        string = 2.0
        with self.assertRaises(TypeError):
            to_upper(string)

    def test_to_upper_functionality(self):
        # Arrange
        string = "Hi, Abebe"

        # Act
        res = to_upper(string)

        # Assert
        self.assertEquals(res, string.upper())


class TestToLower(unittest.TestCase):
    # Write you code here
    def test_to_lower_type(self):
        # check that to_lower fails when the input is not a string
        string = 2.0
        with self.assertRaises(TypeError):
            to_lower(string)

    def test_to_upper(self):
        # Arrange
        string = "HiAbebe"

        # Act
        res = to_lower(string)

        # Assert
        self.assertEquals(res, string.lower())


class TestCapitalize(unittest.TestCase):
    # Write your code here
    def test_capitalize_type(self):
        # check that capitalize fails when the input is not a string
        string = 2.0
        with self.assertRaises(TypeError):
            to_upper(string)

    def test_capitalize(self):
        # Arrange
        string = "hi, Abebe"

        # Act
        res = capitalize(string)

        # Assert
        self.assertEquals(res, string.capitalize())


if __name__ == '__main__':
    unittest.main()
