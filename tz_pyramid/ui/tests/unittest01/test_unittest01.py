import unittest
from mock import patch
from unittest.mock import MagicMock
import tz_pyramid.ui.tests.unittest01.f_test as f_test
from tz_pyramid.ui.tests.unittest01.ProductionClass import ProductionClass

class TestCase1(unittest.TestCase):

    def setUp(self):
        print('before1')

    def tearDown(self):
        print('after1')

    def test_1(self):
        self.assertEqual(1, 1)
        assert 1

    def test_2(self):
        self.assertRaises(ValueError, custom_function, 1)


class TestCase2(unittest.TestCase):

    def setUp(self):
        print('before2')

    def tearDown(self):
        print('after2')

    def test_3(self):
        f_test.method1(1)
        self.assertRaises(ValueError, custom_function, 1)

    def test_4(self):
        self.assertRaises(ValueError, f_test.method2, 2)

        real = ProductionClass()
        real.something = MagicMock()
        real.method()
        real.something.assert_called_once_with(1, 2, 3)

        with patch.object(ProductionClass, 'method') as mock_method:
            mock_method.return_value = None
            real = ProductionClass()
            real.method(1)
            mock_method.assert_called_with(1)

def custom_function(a_1):
    if a_1 == 2:
        return True
    else:
        raise ValueError('error!')


def make_suite(testcase, tests):
    return unittest.TestSuite(map(testcase, tests))


if __name__ == '__main__':
    print("ssss")
    test_suite1 = make_suite(TestCase1, ['test_1', 'test_2'])
    test_suite2 = make_suite(TestCase2, ['test_3', 'test_4'])

    allsuites = unittest.TestSuite([test_suite1, test_suite2])
    allsuites.TextTestRunner(verbosity=2).run(allsuites)
