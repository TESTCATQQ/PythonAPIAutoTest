import requests
import json

data1 = {
    'username':'Junjie',
    'password':'123456'
}

data2 = {
    'username':'Junjie',
    'mobile':'123456',
    'data':'this is data'
}

Testdata = {
'username':'18818227098',
'password':'osWZF5ZpVxSWPUbEJjawADtVXmywd8WikPR48FOeteDrCrRbau70lOotkYRrGMMekSX4xTB/HrilFu/mhLrHXYbpXHaV9m52lUm4LiHbC8TayhyYcMcldY0DDcw0/Qn+8VmHG2gNgbpjmOdRfvx7cVXGoKexeaECmR0WJRXFwmA=',
'verify':'',
'remember':'1',
'pwencode':'1',
'browser_key':'02ccfcc0b4dc2c03a9f10bc83f3cecea',
'referer':'https://www.imooc.com'
}

#url = 'https://www.imooc.com/passport/user/login'
url = 'http://127.0.0.1:8000/login/'

#get


def send_post(url,data):
    res = requests.post(url=url,data=data)
    return res.json()

print(send_post(url,data1))