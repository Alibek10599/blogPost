from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, "hello.html")

def home_page(request):
    return HttpResponse("<h1>Hello world?</h1>")

def about_page(request):
    return HttpResponse("<h1>Hello world?</h1>")