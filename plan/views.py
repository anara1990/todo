from django.shortcuts import render, HttpResponse

# Create your views here.

def example(request):
    return HttpResponse("<h1>This is my first page<h1>")
