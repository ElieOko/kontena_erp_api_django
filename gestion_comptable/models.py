from django.db import models

# Create your models here.


class NoOccurentData(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=40, blank=True, null=False)


class ChartAccount(NoOccurentData):
    code = models.IntegerField(blank=False, null=False)



# class TypeAccount(NoOccurentData):

