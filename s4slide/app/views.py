from django.shortcuts import render
from .forms import databaseSearch

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
    #attempt to read in information from search bar

    if request.method == 'POST':
        form = databaseSearch(request.POST)
        if form.is_valid():
            inputTerm = form.cleaned_data['search']

            print(inputTerm)

    form = databaseSearch()

    return render(request, "viewer.html", {'form': form})
