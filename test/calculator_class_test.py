import unittest #the module

from cpi.calculator import inflation_adjustment

class TestCalculatorClass(unittest.TestCase):

    #check that if start year is less than the conversion year the return should be greater than the amount.
    #if the start year is greater than the conversion year the return should be less than the amount entered.

    
    def calculator_test(self):
       self.assertEqual(inflation_adjustment(10540, 1992), 19206.16)

        


if __name__ == '__main__':
    unittest.main()