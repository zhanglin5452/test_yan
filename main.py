import unittest
from DiffModel.test_login import TestLogin
from DiffModel.test_search import TestSearch
from HTMLTestRunner import HTMLTestRunner

import os

if __name__ == '__main__':

    # test=unittest.defaultTestLoader.discover('./',pattern='test*.py')
    testSuite=unittest.TestSuite()
    # testSuite.addTest(TestLogin('test_login_success'))
    # testSuite.addTest(TestLogin('test_login_fail'))
    testSuite.addTest(TestSearch('test_search'))

    unittest.TextTestRunner().run(testSuite)







