from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
<<<<<<< HEAD
    return HttpResponse("HELLO! WORLD!")
=======
    return render(request, 'get_source/index.html')
>>>>>>> 550b648709ab7241f4c81c2913b334135e244b26
