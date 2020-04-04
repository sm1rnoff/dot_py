# works when list.py is in the same folder. Hence path must be set properly
from list import IntegerList  # import class we are going to test
import unittest  # mandatory

# state to inherit from unittest.TestCase


class TestIntegerList(unittest.TestCase):
    # create specific unit test
    def test_constructor_by_add_and_get_interegers(self):  # starts with test_
        int_list = IntegerList(1, 2, 3, 4, 5)  # prep class for testing
        exp_list = [1, 2, 3, 4, 5]  # prep result
        self.assertEqual(int_list.get_data(), exp_list)  # assert

    def test_add_element_method(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        int_list.add(23)
        exp_list = [1, 2, 3, 4, 5, 23]
        self.assertEqual(int_list.get_data(), exp_list)

    def test_if_added_element_is_not_int_must_return_value_error(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, 'Element is not Integer'):
            int_list.add('six')

    def test_remove_element_and_returns_it(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        expected = [1, 3, 4, 5]
        self.assertEqual(int_list.remove_index(1), 2)
        self.assertEqual(int_list.get_data(), expected)

    def test_remove_element_index_out_of_range_error(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(IndexError, 'Index is out of range'):
            int_list.remove_index(5)

    def test_get_method_returns_specific_element(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(int_list.get(2), 3)

    def test_get_method_returns_out_of_range(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(IndexError, 'Index is out of range'):
            int_list.get(5)


        # mandatory, in order to enable core run when needed only
if __name__ == '__main__':
    unittest.main()
