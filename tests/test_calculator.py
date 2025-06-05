import unittest

from src.calculator import suma, resta, multiplicacion

class CalculatorTest(unittest.TestCase):

    # prueba unitaria para la suma
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
            