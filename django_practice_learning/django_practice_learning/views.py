from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("helo world,  you are at home page")
    return render(request , 'website/index.html')


def about(request):
    return HttpResponse("helo world,  you are at about page")

def contact(request):
    return HttpResponse("helo world,  you are at contact page")

