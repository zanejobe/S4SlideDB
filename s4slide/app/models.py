from django.db import models


#**********************************************************************
#* SUMMARY_INFO_ID
#* 
#* CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
#*      - Parent ID
#*      - Object Type 
#**********************************************************************/
class summary_info_id (models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    name = models.CharField(max_length = 50)
    aliases = models.CharField(max_length = 50) 
    frontal_confinement = models.BooleanField()
    object_type = models.BooleanField()
    ss_depth_m = models.FloatField()
    ss_time_twtt = models.FloatField()
    ss_depth_notes = models.TextField()
    def __str__(self):
        return self.name
#/**********************************************************************
# * LANDSLIDE MORPHOMETRICS
# *
# * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
# *      - Scarp Surf Nat 
# *          - What kind of data type is this? String?
# *          - If it is a string, how long should the string be
# **********************************************************************/
class landslide_morphometrics (models.Model):
    id = models.AutoField(primary_key=True)
    landslide_id = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField()
    w_depth_min = models.FloatField()
    w_depth_max = models.FloatField()
    w_depth_notes = models.FloatField()
    lt = models.FloatField()
    ld = models.FloatField()
    le = models.FloatField()
    l_notes = models.TextField()
    ls = models.FloatField()
    hs = models.FloatField()
    he = models.FloatField()
    ws = models.FloatField()
    scarp_surf_nat = models.CharField(max_length = 50)
    scarp_notes = models.TextField()
    wd = models.FloatField()
    td_max_m = models.FloatField()
    td_max_twtt = models.FloatField()
    tu_max_m = models.FloatField()
    tu_max_twtt = models.FloatField()
    t_notes = models.TextField()
    dep_notes = models.TextField()
    ht = models.FloatField()
    s = models.FloatField()
    s_notes = models.TextField()
    ss = models.FloatField()
    ss_notes = models.TextField()
    st = models.FloatField()
    st_notes = models.TextField()
#    def __str__(self):
#        return self.name

#/**********************************************************************
# * LANDSLIDE METRICS
# *
# * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
# *      - Age error
# **********************************************************************/
class landslide_metrics (models.Model):
    id = models.AutoField(primary_key=True)
    landslide_id = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
    attachment = models.BooleanField()
    surf_basal = models.CharField(max_length = 50)
    surf_upper = models.CharField(max_length = 50)
    a = models.FloatField()
    a_notes = models.TextField()
    v = models.FloatField()
    v_notes = models.TextField()
    age = models.IntegerField()
    age_error = models.BooleanField()
    age_notes = models.TextField()
    features = models.TextField()
#    def __str__(self):
#        return self.name

#/**********************************************************************
# * META TABLE
# *
# * CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
# *      - Data Sources (strictly a link?)
# *      - Data Repo (strictly a link?)
# *      - Pub (strictly a link?)
# *      - Data resolution horizontal 
# *          - (is this an int or float, what are the units)
# *          - what are the units on this? pixel?
# *      - Data resolution vertical 
# *          - (is this an int or float, what are the units)
# *          - what are the units on this? pixel?
# **********************************************************************/
class meta_table (models.Model):
    id = models.AutoField(primary_key=True)
    landslide_id = models.ForeignKey('summary_info_id', on_delete=models.CASCADE,)
    data_type = models.CharField(max_length = 50)
    data_type_notes = models.TextField()
    data_source = models.CharField(max_length = 100)
    data_repo = models.CharField(max_length = 100)
    pub = models.CharField(max_length = 100)
    contact_name = models.CharField(max_length = 50)
    contact_email = models.CharField(max_length = 50)
    db_contact_name = models.CharField(max_length = 50)
    db_contact_email = models.CharField(max_length = 50)
    db_notes = models.TextField()
    data_res_h = models.IntegerField()
    data_res_v = models.IntegerField()
    notes = models.TextField()
#    def __str__(self):
#        return self.name