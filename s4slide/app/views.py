from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def contribute(request):
    return render(request, "contribute.html")

def landslide(request):
    return render(request, "landslide.html")

def links(request):
    return render(request, "links.html")

def people(request):
    return render(request, "people.html")

def viewer(request):
    return render(request, "viewer.html")
