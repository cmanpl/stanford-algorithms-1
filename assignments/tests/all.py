__author__ = 'cman'

import unittest
import assignment_one

MODULES = [assignment_one]
SUITES = [m.suite() for m in MODULES]

runner = unittest.TextTestRunner()
runner.run(unittest.TestSuite(SUITES))