import unittest
from package.demo2 import RunMain
import json
#from demo import RunMain

class TestMethod(unittest.TestCase):

    # def __init__(self):
    #     print(1)

    def setUp(self):
        self.run = RunMain()
        self.url = 'http://127.0.0.1:8000/login/'
    
    def tearDown(self):
        print('End')

    def test_01(self):
        data1 = {
        'username':'Junjie',
        'password':'123456'
        }
        res = self.run.run_main(self.url,'POST',data1)
        #print(type(res)) str?
        print(res)
    
    def test_02(self):
        url2 = 'http://127.0.0.1:8000/login/'
        data2 = {
        'username':'ZhaoJunjie',
        'password':'12345678'
        }
        res = self.run.run_main(url2,'POST',data2)
        #print(json.loads(res,indent=2,sort_keys=True))
        print(json.dumps(res,indent=2,sort_keys=True))
        print('This is second unittest')


if __name__ == '__main__':
    unittest.main()
    
