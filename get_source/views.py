from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    params = {
        'title':'SAMPLE',
        'msg':'これはサンプルページです。',
        'goto':'next',
    }
    return render(request, 'get_source/index.html', params)

def next(request):
    params = {
        'title':'SAMPLE_2',
        'msg':'これは遷移ページです。',
        'goto':'index',
    }
    return render(request, 'get_source/index.html', params)