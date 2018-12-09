from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse(username)
    else:
        return render_to_response('login.html')