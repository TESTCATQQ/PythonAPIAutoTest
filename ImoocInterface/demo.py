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

res = requests.post(url = 'http://127.0.0.1:8000/login/',data = data1)
print(res.text)