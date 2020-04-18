from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView 

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, you just configured your First URL</h1>")

def page(request):
    return redirect('/adminpage')

class TutorialA(RedirectView):
    url = 'http://google.co.in/'

def inf1(request):
    return redirect('/inf2')
def inf2(request):
    return redirect('/inf1')