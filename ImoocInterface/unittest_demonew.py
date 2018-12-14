import unittest

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类执行前的方法')
    
    @classmethod
    def tearDownClass(cls):
        print('类执行后的方法')
    #每次方法之前执行
    def setUp(self):
        print('test-->setup')
    #每次方法之后执行
    def tearDown(self):
        print('test-->tearDown')

    def test_01(self):
        print('Try my first test.')
    
    def test_02(self):
        print('Try my second test.')
    
    def test_03(self):
        print('Try my third test.')

if __name__ == '__main__':
    unittest.main()
    
