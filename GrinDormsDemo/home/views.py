from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
    link_list = {'browse', 'review'}
    context = {"link_list": link_list}
    return render(request, "home/home.html", context)
