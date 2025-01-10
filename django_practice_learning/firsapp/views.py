from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def all(request):
    return render(request , 'firsapp/all.html')
    # return HttpResponse("hello world, you are at all page")
