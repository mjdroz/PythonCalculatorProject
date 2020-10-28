import unittest
from Calculator import Calculator
from CSVReader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('/src/UnitTests/UnitTestAddition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CSVReader('/src/UnitTests/UnitTestSubtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result,int(row['Result']))

if __name__ == '__main__':
    unittest.main()
