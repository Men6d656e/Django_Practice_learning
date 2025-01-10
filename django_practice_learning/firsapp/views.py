from django.http import HttpResponse
from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404



# Create your views here.
def all(request):
    chais = ChaiVarity.objects.all()
    return render(request , 'firsapp/all.html' , { 'chais' : chais })
    # return HttpResponse("hello world, you are at all page")


def chai_details(request , chai_id):
    chai = get_object_or_404(ChaiVarity , pk = chai_id)
    return render(request , 'firsapp/chai_details.html' , { 'chai' : chai })