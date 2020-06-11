from django.db import models

class summary_info_id(models.Model):
	pid = models.IntegerField(null=True)
	name = models.TextField()
	aliases = models.TextField() 
	frontal_confinement = models.BooleanField(null=True)
	TYPE_CHOICES = [("S", "Single"), ("M", "Multiple")]
	object_type = models.CharField(max_length=1, choices=TYPE_CHOICES) # TODO check that pid is not null if multiple
	ss_depth_m = models.FloatField(null=True)
	ss_time_twtt = models.FloatField(null=True)
	ss_depth_notes = models.TextField()
	comments = models.TextField()
	category = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["id"]

class landslide_morphometrics(summary_info_id):
	landslide = models.OneToOneField(
			summary_info_id, on_delete=models.CASCADE,
			parent_link=True, primary_key=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	w_depth_min = models.FloatField(null=True)
	w_depth_max = models.FloatField(null=True)
	w_depth_notes = models.TextField()
	lt = models.FloatField(null=True)
	ld = models.FloatField(null=True)
	le = models.FloatField(null=True)
	l_notes = models.TextField()
	ls = models.FloatField(null=True)
	hs = models.FloatField(null=True)
	he = models.FloatField(null=True)
	ws = models.FloatField(null=True)
	scarp_surf_nat = models.TextField()
	scarp_notes = models.TextField()
	wd = models.FloatField(null=True)
	td_max_m = models.FloatField(null=True)
	td_max_twtt = models.FloatField(null=True)
	tu_max_m = models.FloatField(null=True)
	tu_max_twtt = models.FloatField(null=True)
	t_notes = models.TextField()
	dep_notes = models.TextField()
	ht = models.FloatField(null=True)
	s = models.FloatField(null=True)
	s_notes = models.TextField()
	ss = models.FloatField(null=True)
	ss_notes = models.TextField()
	st = models.FloatField(null=True)
	st_notes = models.TextField()

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=["latitude", "longitude"], name="unique_latlong")
		]
		ordering = ["landslide"]

class landslide_metrics(summary_info_id):
	landslide = models.OneToOneField(
			summary_info_id, on_delete=models.CASCADE,
			parent_link=True, primary_key=True)
	attachment = models.BooleanField(null=True)
	surf_basal = models.TextField()
	surf_upper = models.TextField()
	a = models.FloatField(null=True)
	a_notes = models.TextField()
	v = models.FloatField(null=True)
	v_notes = models.TextField()
	age = models.TextField()
	age_error = models.FloatField(null=True)
	age_notes = models.TextField()
	features = models.TextField()

	class Meta:
		ordering = ["landslide"]

class meta_table(summary_info_id):
	landslide = models.OneToOneField(
			summary_info_id, on_delete=models.CASCADE,
			parent_link=True, primary_key=True)
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

