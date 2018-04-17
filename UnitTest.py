import unittest
from randomnum import codegenerator


class MyTest(unittest.TestCase):
    def test(self):

        self.assertNotEquals(codegenerator.Random().random_num(), 1234)
if __name__=='__main__':
    unittest.main()
