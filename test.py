import unittest
import class_example
# import pytest


#@pytest.mark.usefixtures("class_example")
class TestMyModule(unittest.TestCase):
    # @pytest.fixture(autouse=True)
    def setUp(self):
        return
    # @pytest.fixture(autouse=True)
    def test_do_divide(self):

        fist_arg = 4
        second_arg = 2

        result = class_example.do_divide(fist_arg,second_arg)
        expected_result = 2
        self.assertEqual(result, expected_result)
    # @pytest.fixture(autouse=True)
    def test_do_divide_by_zero(self):

        fist_arg = 4
        second_arg = 0

        result = class_example.do_divide(fist_arg,second_arg)
        expected_result = None
        self.assertEqual(result, expected_result)
