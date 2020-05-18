from django.db import models


#**********************************************************************
#* SUMMARY_INFO_ID
#* 
#* CONFUSED ABOUT THE DATA TYPE FOR THE FOLLOWING VARIABLES: 
#*      - Parent ID
#*      - Object Type 
#**********************************************************************/
class summary_info_id (models.Model):
    #id = models.AutoField(primary_key=True), - already automatic
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
