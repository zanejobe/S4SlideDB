from django.shortcuts import render
from .forms import databaseSearch
from .models import summary_info_id

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
	if len(request.GET) > 0:
		form = databaseSearch(request.GET)
		if form.is_valid():
			data = summary_info_id.objects.filter(name__contains=request.GET["search"]).values()
	else:
		form = databaseSearch()
		data = {}
	return render(request, "viewer.html", {"form": form, "data": data})

