from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def MyPersonalWebsite(request):
    return render(request, "MyPersonalWebsite.html")

def PCParts(request):
    return render(request, "PCParts.html")
