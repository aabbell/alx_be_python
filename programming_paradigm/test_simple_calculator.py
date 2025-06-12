from simple_calculator import SimpleCalculator
import unittest




class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2 ,2), 0)
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(5 ,10), -5)
        self.assertEqual(self.calc.subtract(-3 ,-3) ,0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2 ,2) ,4)
        self.assertEqual(self.calc.multiply(0, 10) ,0)
        self.assertEqual(self.calc.multiply(-2 ,3) ,-6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

        # Test divide by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)



if __name__ == '__main__':
    unittest.main()