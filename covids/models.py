from django.db import models

class Covid(models.Model):
    area    = models.CharField(max_length=100 ,    blank=True , null=True)
    country = models.CharField(max_length=200 ,    blank=True , null=True)
    patient = models.IntegerField(max_length=500 , blank=True , null=True)
    dead    = models.IntegerField(max_length=500 , blank=True , null=True)

    class Meta:
        db_table = 'covids'

class KoreaCovid(models.Model):
    area     = models.CharField(max_length=100,    blank=True , null=True)
    patient  = models.IntegerField(max_length=500, blank=True , null=True)
    increase = models.CharField(max_length=250,    blank=True , null=True)

    class Meta:
        db_table = "korea_covids"
