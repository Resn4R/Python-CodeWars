import unittest
from Katas.kata7 import stringCalculator

'''
Create a simple calculator that takes a String and returns a integer

Signature (pseudo code):
int Add(string numbers)
Requirements

1. The method can take up to two numbers, separated by commas, and will return their sum as a result. So the inputs can be: “”, “1”, “1,2”. For an empty string, it will return 0.
'''

class Test_StringCalculator(unittest.TestCase):

    def test_Requirement1(self):
        string = ','
        sampleResult = stringCalculator(string)
        self.assertEqual(sampleResult, 0, "empty strings should return 0")

    def test_Requirement1(self):
        string = '1,'
        sampleResult = stringCalculator(string)
        self.assertEqual(sampleResult, 1, f"sum of '{string}' should be 1")