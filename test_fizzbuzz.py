import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_given_3_return_Fizz(self):
        self.assertEqual(fizzbuzz.process(3), 'Fizz')
    
    def test_given_number_divisible_by_3_return_Fizz(self):
        self.assertEqual(fizzbuzz.process(3), 'Fizz')
        self.assertEqual(fizzbuzz.process(6), 'Fizz')
        self.assertEqual(fizzbuzz.process(9), 'Fizz')
        self.assertEqual(fizzbuzz.process(12), 'Fizz')
    
    def test_given_number_divisible_by_5_return_Buzz(self):
        self.assertEqual(fizzbuzz.process(5), 'Buzz')
        self.assertEqual(fizzbuzz.process(20), 'Buzz')
        self.assertEqual(fizzbuzz.process(40), 'Buzz')
        self.assertEqual(fizzbuzz.process(80), 'Buzz')

    def test_given_number_divisible_by_both_3_5_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz.process(30), 'FizzBuzz')
        self.assertEqual(fizzbuzz.process(60), 'FizzBuzz')
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz.process(45), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()