import unittest
import class_example

class TestMyModule(unittest.TestCase):

    def setUp(self):
        return

    # @pytest.fixture
    def test_do_divide(self):

        fist_arg = 4
        second_arg = 2

        result = class_example.do_divide(fist_arg,second_arg)
        expected_result = 2
        self.assertEqual(result, expected_result)

#     # @pytest.fixture
#     def test_do_divide_by_zero(self):

#         fist_arg = 4
#         second_arg = 2

#         result = class_example.do_divide(fist_arg,second_arg)
#         expected_result = None
#         self.assertEqual(result, expected_result)

# # if __name__ =="main":
#     # unittest.main()