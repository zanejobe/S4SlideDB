from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .forms import databaseSearch
from .models import *
import json

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
			sum_qs = summary_info_id.objects.filter(name__contains=request.GET["search"])
			morpho = landslide_morphometrics.objects.filter(landslide__in=sum_qs).values()
			metrics = landslide_metrics.objects.filter(landslide__in=sum_qs).values()
			meta = meta_table.objects.filter(landslide__in=sum_qs).values()
			data = zip(sum_qs.values(), morpho, metrics, meta)
	else:
		form = databaseSearch()
		data = zip()
	return render(request, "viewer.html", {"form": form, "data": data})

def upload(request):
	data = json.loads(request.POST["data"])
	for row in data:
		summary = summary_info_id(**row["sum"])
		summary.save()
		morpho = landslide_morphometrics(**row["morpho"], landslide=summary)
		morpho.save()
		metrics = landslide_metrics(**row["metrics"], landslide=summary)
		metrics.save()
		meta = meta_table(**row["meta"], landslide=summary,
				contact_name=request.POST["name"], contact_email=request.POST["email"])
		meta.save()
	return HttpResponse("")

@xframe_options_sameorigin
def map(request):
	return render(request, "map.html");

@xframe_options_sameorigin
def plot(request):
	return render(request, "plot.html");
