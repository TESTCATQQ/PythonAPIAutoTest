import requests
import json

class Run_Main:
    
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_get(self,url,data):
        res = requests.get(url=url,data=None).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
     #POST
    url1 = 'http://127.0.0.1:8000/login/'
    #GET
    url2 = 'http://127.0.0.1:8000/loginget/'

    data1 = {
        'username':'Junjie',
        'password':'123456'
    }

    data2 = {
        'username':'Junjie',
        'mobile':'123456',
        'data':'this is data'
    }

    myrun = Run_Main()
    res = myrun.run_main(url1,'POST',data1)
    print(res)