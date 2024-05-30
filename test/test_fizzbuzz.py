import unittest
from Katas.kata6 import isfizzbuzz
'''
fizzbuzz 
if n % 3 = fiz
if n % 5 = buzz
if n % 3 and 5 = fizzbuzz
'''

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_1_should_return_1(self):
        number = 1
        sampleFB = isfizzbuzz(number)
        self.assertEqual(sampleFB, str(number), f"Result should be {number}, as the number is divisible by 3")

    def test_fizz_2_should_return_2(self):
        number = 2
        sampleFB = isfizzbuzz(number)
        self.assertEqual(sampleFB, str(number), f"Result should be {number}, as the number is divisible by 3")

    def test_fizz_3_should_return_fizz(self):
        number = 3
        sampleFB = isfizzbuzz(number)
        self.assertEqual(sampleFB, "fizz", "Result should be fizz, as the number is divisible by 3")

    def test_fizz_5_should_return_buzz(self):
        number = 5
        sampleFB = isfizzbuzz(number)
        self.assertEqual(sampleFB, "buzz", "Result should be buzz, as the number is divisible by 3")

    def test_fizz_15_should_return_buzz(self):
        number = 15
        sampleFB = isfizzbuzz(number)
        self.assertEqual(sampleFB, "fizzbuzz", "Result should be fizzbuzz, as the number is divisible by 3")