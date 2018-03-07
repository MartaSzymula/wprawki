import unittest
import script_01

class Test_task8(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_653(self):
        self.assertEqual( script_01.task8(653), 'six five three')

    def test_strings_a10(self):
        self.assertEqual( script_01.task8('a10'), 'one zero')


if __name__ == '__main__':
    unittest.main()
