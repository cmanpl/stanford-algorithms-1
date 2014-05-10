__author__ = 'cman'

import unittest
import merge_sort


MODULES = [merge_sort]
SUITES = [m.suite() for m in MODULES]

runner = unittest.TextTestRunner()
runner.run(unittest.TestSuite(SUITES))
