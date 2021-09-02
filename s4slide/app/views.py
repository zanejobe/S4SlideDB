from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.db import transaction
from django.db.models import Count, Q
from .forms import databaseSearch
from .models import *
import json

def index(request):
	return render(request, "index.html")

# TODO set up caching for this view
def contribute(request):
	# generate a list of contributors
	# ordering by most (verified) contributions
	# limit to 100 rows, so it's not too long
	data = meta_table.objects.filter(verified=True).values("contact_name", "contact_email").annotate(contributions=Count("landslide")).order_by("-contributions")[:100]
	return render(request, "contribute.html", {"data": data})

def landslide(request):
	return render(request, "landslide.html")

def links(request):
	return render(request, "links.html")

def about(request):
	return render(request, "about.html")

def viewer(request):
	if len(request.GET) > 0:
		form = databaseSearch(request.GET)
		if form.is_valid():
			sum_qs = summary_info_id.objects.none()

			if form.cleaned_data["name"]:
				name_qs = summary_info_id.objects.filter(Q(name__icontains=form.cleaned_data["name"]) |
					Q(alias__icontains=form.cleaned_data["name"]))
				idList = name_qs.values_list("id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			if form.cleaned_data["age"]:
				age_qs = landslide_metrics.objects.filter(age__icontains=form.cleaned_data["age"])
				idList = age_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			if form.cleaned_data["cont"]:
				cont_qs = meta_table.objects.filter(contact_name__icontains=form.cleaned_data["cont"])
				idList = cont_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			if form.cleaned_data["lat_start"] and form.cleaned_data["lat_end"]:
				lat_qs = landslide_morphometrics.objects.filter(latitude__range=(
					form.cleaned_data["lat_start"],
					form.cleaned_data["lat_end"]))
				idList = lat_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			if form.cleaned_data["lng_start"] and form.cleaned_data["lng_end"]:
				lng_qs = landslide_morphometrics.objects.filter(longitude__range=(
					form.cleaned_data["lng_start"],
					form.cleaned_data["lng_end"]))
				idList = lng_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			if form.cleaned_data["date_start"] and form.cleaned_data["date_end"]:
				date_qs = meta_table.objects.filter(upload_date__range=(
					form.cleaned_data["date_start"],
					form.cleaned_data["date_end"]))
				idList = date_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			elif form.cleaned_data["date_start"] and not form.cleaned_data["date_end"]:
				date_qs = meta_table.objects.filter(upload_date__gte=form.cleaned_data["date_start"])
				idList = date_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			elif not form.cleaned_data["date_start"] and form.cleaned_data["date_end"]:
				date_qs = meta_table.objects.filter(upload_date__lte=form.cleaned_data["date_end"])
				idList = date_qs.values_list("landslide_id", flat=True)
				sum_qs |= summary_info_id.objects.filter(id__in=idList)

			morpho = landslide_morphometrics.objects.filter(landslide__in=sum_qs).values()
			metrics = landslide_metrics.objects.filter(landslide__in=sum_qs).values()
			meta = meta_table.objects.filter(landslide__in=sum_qs).values()
			data = zip(sum_qs.values(), morpho, metrics, meta)
		else:
			data = zip()
	else:
		'''
		Displaying all data by default now
		'''
		form = databaseSearch()
		sum_qs = summary_info_id.objects.all()
		morpho = landslide_morphometrics.objects.filter(landslide__in=sum_qs).values()
		metrics = landslide_metrics.objects.filter(landslide__in=sum_qs).values()
		meta = meta_table.objects.filter(landslide__in=sum_qs).values()
		data = zip(sum_qs.values(), morpho, metrics, meta)

		'''form = databaseSearch()
		data = zip()'''

	return render(request, "viewer.html", {"form": form, "data": data})

# wrap this view in a transaction
# if there is an error saving one row
# none of the rows will be saved
# and a server error will be generated
@transaction.atomic
def upload(request):
	data = json.loads(request.POST["data"])
	for row in data:
		summary = summary_info_id(**row["sum"])
		# summary needs to be saved first to calculate the id
		summary.full_clean()
		summary.save()
		# generate a default name if there was none provided
		if not summary.name:
			summary.name = "Landslide {}".format(summary.id)
			summary.save()
		morpho = landslide_morphometrics(**row["morpho"], landslide=summary)
		metrics = landslide_metrics(**row["metrics"], landslide=summary)
		meta = meta_table(**row["meta"], landslide=summary,
				contact_name=request.POST["name"], contact_email=request.POST["email"])
		morpho.full_clean()
		metrics.full_clean()
		meta.full_clean()
		morpho.save()
		metrics.save()
		meta.save()
	return HttpResponse("")

@xframe_options_sameorigin
def map(request):
	return render(request, "map.html");

@xframe_options_sameorigin
def plot(request):
	return render(request, "plot.html");
