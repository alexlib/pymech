import numpy as np

import unittest
import pymech.print.Latex as Latex
from pymech.units.SI import ureg
import math as math

class test_print_methods(unittest.TestCase):

    def test_array(self):
        test_arr3_4 = [[1,2,3,r"\sigma_0"],[4,5,6, r"\sigma_1"], [7, 8, 9, r"\sigma_2"]]
        test_arr1_2 = [[1],[r"\sigma_0"]]
        self.assertEqual(Latex.array(test_arr3_4),'\\begin{array}{ccc}1.00E+00&2.00E+00&3.00E+00&\\sigma_0\\\\ 4.00E+00&5.00E+00&6.00E+00&\\sigma_1\\\\ 7.00E+00&8.00E+00&9.00E+00&\\sigma_2\\end{array}')
        self.assertEqual(Latex.array(test_arr1_2), '\\begin{array}{c}1.00E+00\\\\ \\sigma_0\\end{array}')

    def test_toStr(self):
        testStr = r"\sigma"
        testFloat = 0.666
        testInt = 666

        self.assertEqual(Latex.toStr(testStr), "\\sigma")
        self.assertEqual(Latex.toStr(testFloat), '6.66E-01')
        self.assertEqual(Latex.toStr(testInt), '6.66E+02')

    def test_sqrt(self):
        self.assertEqual(Latex.sqrt(5), '\\sqrt{5.00E+00}')
        self.assertEqual(Latex.sqrt(5,3), '\\sqrt[3]{5.00E+00}')

    def test_unit(self):
        test_unit_n = 0.666 * ureg.N
        test_unit_a = 3.333 * ureg.mm ** 2
        test_unit = test_unit_n / test_unit_a

        self.assertEqual(Latex.toStr(test_unit), '2.00E-01 [newton / millimeter^{2}]')

    def test_combined(self):
        test_unit_n = 0.666 * ureg.N ** 2
        test_unit_a = 3.333 * ureg.mm ** 200
        test_unit_p = test_unit_n / test_unit_a
        test_result = math.sqrt(test_unit_p.magnitude) * ureg.Pa * ureg.m ** -98
        self.assertEqual(Latex.Latex(Latex.sqrt(Latex.frac(test_unit_n, test_unit_a)) + r" = " + Latex.toStr(test_result)), '$\\sqrt{\\frac{6.66E-01 [newton^{2}]}{3.33E+00 [millimeter^{200}]}} = 4.47E-01 [pascal / meter^{98}]$')