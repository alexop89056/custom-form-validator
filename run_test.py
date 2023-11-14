import unittest
from tests import TestFormPositive, TestFormNegative

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFormPositive))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFormNegative))
    unittest.TextTestRunner().run(test_suite)