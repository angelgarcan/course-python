import sys

sys.path.append("./")

import unittest
import logging
import src.calculator as calc

logging.basicConfig(filename="testing.log", format='%(asctime)s %(message)s', filemode="a")
LOG_WRITER = logging.getLogger()
LOG_WRITER.setLevel(logging.DEBUG)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        LOG_WRITER.info("Starting Calculator tests")
        self.first_number = 100
        self.second_number = 50
        self.calc = calc.BasicCalculator()

    def tearDown(self):
        LOG_WRITER.info("Finishing Calculator test")

    def test_addition(self):
        result = self.calc.addition(self.first_number, self.second_number)
        self.assertEqual(result, 150)

    def test_substraction(self):
        result = self.calc.substraction(self.first_number, self.second_number)
        self.assertEqual(result, 50)

    def test_square_power(self):
        result = self.calc.square_power(50)
        self.assertGreater(result, 50)

if __name__=="__main__":
    unittest.main()