__author__ = 'cman'

import unittest
import assignment_one
import assignment_two
import assignment_four

MODULES = [assignment_one, assignment_two, assignment_four]
SUITES = [m.suite() for m in MODULES]

runner = unittest.TextTestRunner()
runner.run(unittest.TestSuite(SUITES))