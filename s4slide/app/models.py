from django.db import models


class summary_info_id (models.Model):
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

class landslide_morphometrics (models.Model):
	landslide = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
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

class landslide_metrics (models.Model):
	landslide = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
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

class meta_table (models.Model):
	landslide = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
	data_type = models.TextField()
	data_type_notes = models.TextField()
	data_source = models.TextField()
	data_repo = models.TextField()
	pub = models.TextField()
	contact_name = models.TextField()
	contact_email = models.TextField()
	db_notes = models.TextField()
	data_res_h = models.FloatField(null=True)
	data_res_v = models.FloatField(null=True)
	notes = models.TextField()
	upload_date = models.DateTimeField(auto_now_add=True)
	verified = models.BooleanField(default=False)

