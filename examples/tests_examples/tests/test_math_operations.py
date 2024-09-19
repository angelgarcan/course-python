import unittest
import logging

logging.basicConfig(filename="testing.log", format='%(asctime)s %(message)s', filemode="a")
LOG_WRITER = logging.getLogger()
LOG_WRITER.setLevel(logging.DEBUG)

class TestMathOps(unittest.TestCase):
    def setUp(self):
        LOG_WRITER.info("Setting Math Ops test variables")
        self.zero_module = 2%2
    
    def tearDown(self):
       LOG_WRITER.info("Math Ops test Finished")

    def test_equal(self):
        addition = 5 + 5
        self.assertEqual(addition, 10)
        self.assertNotEqual(addition, 100)
        LOG_WRITER.info("test_equal finished")

    def test_boolean(self):
        substraction = 5 - 5
        square_number = 5**2
        self.assertFalse(substraction == 10)
        self.assertTrue(square_number == 25)
        LOG_WRITER.info("test_boolean finished")

    def test_setup_variables(self):
        self.assertEqual(self.zero_module, 0)
        LOG_WRITER.info("test_setup_variables finished")

if __name__=="__main__":
    unittest.main()