import unittest
import letter_counter

class Test_task8(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_653(self):
        self.assertEqual( letter_counter.task8(653), 'six five three')

    def test_strings_a10(self):
        self.assertEqual( letter_counter.task8('a10'), 'one zero')

    def test_strings_one51(self):
        self.assertEqual( letter_counter.task8('one 51'), 'one five one')


class Test_task9(unittest.TestCase):

    def setUp(self):
        pass

    def test_two_floats(self):
        self.assertEqual( letter_counter.task9(3.5, 4.5), 4)

    def test_list_params(self):
        self.assertEqual( letter_counter.task9([1, 0, 2]), 1)




if __name__ == '__main__':
    unittest.main(verbosity=2)
