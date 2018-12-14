import unittest
from demo import Run_Main

class TestMethod(unittest.TestCase):

    def test_01(self):
        print('Try my first test.')
    
    def test_02(self):
        print('Try my second test.')


if __name__ == '__main__':
    unittest.main()
    
