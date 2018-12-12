from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.
def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['user'] = username
        result['pass'] = password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
        #'dict' object has no attribute 'POST'
        #cause,"password = result.POST.get('
    else:
        return render_to_response('login.html')

def LoginGet(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        data = request.GET.get('data')
        #Can;t response two or more results
        result['user'] = username
        result['mobile'] = mobile
        result['data'] = data
        result = json.dumps(result)
        #return  HttpResponse(username)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('loginget.html')