
import unittest
from helpers.Example import Example

class ExampleTest(unittest.TestCase) :

    def test_GetValue(self) :
        self.assertEqual(Example().GetVal(), 1)

