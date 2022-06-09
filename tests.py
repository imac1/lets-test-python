import unittest
import functions

class BasicTestCase(unittest.TestCase):
    def test_add_two_integers(self):
        a = 5
        b = 10
        expected_result = a + b
        actual_result = functions.add_two_integers(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_is_integer_a_greater_than_integer_b(self):
        a = 5
        b = 10
        expected_result = False
        actual_result = functions.is_integer_a_greater_than_integer_b(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_say_hello(self):
        name = "Marcus"
        expected_result = "Hello, Marcus!"
        actual_result = functions.say_hello(name)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
