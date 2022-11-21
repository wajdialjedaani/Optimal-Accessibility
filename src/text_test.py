""" Unit tests for text.py """
import unittest
from text import shall_return_foo


class TestTextRecognition(unittest.TestCase):
    """ All unit tests for text recognition is within this class """

    def test_upper(self):
        """ Asserts "foo".upper() is equal to "FOO" """
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        """ Asserts "Foo".isupper() is not equal to "FOO" """
        self.assertFalse("Foo".isupper())

    def test_split(self):
        """ Asserts "hello wrold" can not be separated """
        hello_world_str = "hello world"
        self.assertEqual(hello_world_str.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            hello_world_str.split(2)

    def test_foo(self):
        """ Asserts shall_return_foo returns "FOO" """
        my_foo_str = shall_return_foo()
        self.assertEqual(my_foo_str, "FOO")


if __name__ == "__main__":
    unittest.main()
