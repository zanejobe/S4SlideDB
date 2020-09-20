from django.db import models
from django.core.exceptions import ValidationError

class summary_info_id(models.Model):
	# TODO parent is currently unused
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True);
	name = models.CharField(max_length=100, blank=True)
	alias = models.CharField(max_length=100, blank=True)
	frontal_confinement = models.BooleanField(null=True, blank=True)
	TYPE_CHOICES = [("S", "Single"), ("M", "Multiple")]
	object_type = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True)
	ss_depth_m = models.FloatField(null=True, blank=True)
	ss_time_twtt = models.FloatField(null=True, blank=True)
	ss_depth_notes = models.TextField(blank=True)
	comments = models.TextField(blank=True)
	category = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name

	def clean(self):
		references = summary_info_id.objects.filter(parent__exact=self.id).count()
		if self.object_type == "S" and references > 0:
			raise ValidationError(_("Single objects must not be referenced as a parent."))
		if self.object_type == "M":
			if self.parent is not None:
				raise ValidationError(_("Multiple objects may not reference a parent."))
			if references < 1:
				raise ValidationError(_("Multiple objects must have one or more references as a parent."))

	class Meta:
		ordering = ["id"]

class landslide_morphometrics(models.Model):
	landslide = models.OneToOneField(summary_info_id, on_delete=models.CASCADE, primary_key=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	w_depth_min = models.FloatField(null=True, blank=True)
	w_depth_max = models.FloatField(null=True, blank=True)
	w_depth_notes = models.TextField(blank=True)
	lt = models.FloatField(null=True, blank=True)
	ld = models.FloatField(null=True, blank=True)
	le = models.FloatField(null=True, blank=True)
	l_notes = models.TextField(blank=True)
	ls = models.FloatField(null=True, blank=True)
	hs = models.FloatField(null=True, blank=True)
	he = models.FloatField(null=True, blank=True)
	ws = models.FloatField(null=True, blank=True)
	scarp_surf_nat = models.TextField(blank=True)
	scarp_notes = models.TextField(blank=True)
	wd = models.FloatField(null=True, blank=True)
	td_max_m = models.FloatField(null=True, blank=True)
	td_max_twtt = models.FloatField(null=True, blank=True)
	tu_max_m = models.FloatField(null=True, blank=True)
	tu_max_twtt = models.FloatField(null=True, blank=True)
	t_notes = models.TextField(blank=True)
	dep_notes = models.TextField(blank=True)
	ht = models.FloatField(null=True, blank=True)
	s = models.FloatField(null=True, blank=True)
	s_notes = models.TextField(blank=True)
	ss = models.FloatField(null=True, blank=True)
	ss_notes = models.TextField(blank=True)
	st = models.FloatField(null=True, blank=True)
	st_notes = models.TextField(blank=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=["latitude", "longitude"], name="unique_latlong")
		]
		ordering = ["landslide"]

class landslide_metrics(models.Model):
	landslide = models.OneToOneField(summary_info_id, on_delete=models.CASCADE, primary_key=True)
	attachment = models.BooleanField(null=True, blank=True)
	surf_basal = models.CharField(max_length=25, blank=True)
	surf_upper = models.TextField(max_length=25, blank=True)
	a = models.FloatField(null=True, blank=True)
	a_notes = models.TextField(blank=True)
	v = models.FloatField(null=True, blank=True)
	v_notes = models.TextField(blank=True)
	age = models.CharField(max_length=50, blank=True)
	age_error = models.CharField(max_length=50, blank=True)
	age_notes = models.TextField(blank=True)
	features = models.TextField(blank=True)

	class Meta:
		ordering = ["landslide"]

class meta_table(models.Model):
	landslide = models.OneToOneField(summary_info_id, on_delete=models.CASCADE, primary_key=True)
	data_type = models.TextField(blank=True)
	data_type_notes = models.TextField(blank=True)
	data_source = models.TextField(blank=True)
	data_repo = models.TextField(blank=True)
	pub = models.TextField(blank=True)
	contact_name = models.CharField(max_length=50)
	contact_email = models.EmailField()
	db_notes = models.TextField(blank=True)
	data_res_h = models.FloatField(null=True, blank=True)
	data_res_v = models.FloatField(null=True, blank=True)
	notes = models.TextField(blank=True)
	upload_date = models.DateTimeField(auto_now_add=True)
	verified = models.BooleanField(default=False)

	class Meta:
		ordering = ["landslide"]

