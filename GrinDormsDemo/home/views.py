from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
    #probably need to make a model that stores the apps we want to integrate so this isn't as hard coded
    link_list = {'browse', 'review'}
    context = {"link_list": link_list}
    return render(request, "home/home.html", context)
