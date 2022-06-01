from django.db import models

# Create your models here.


class Population(models.Model):
    population = models.CharField(max_length=80)
    avg_age = models.IntegerField()


class WorldFertility(models.Model):
    country = models.CharField(max_length=80, blank=True, null=True)
    fertility = models.FloatField(blank=True, null=True)
    iso_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_fertility'
