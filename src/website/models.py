# Register your models here
from django.db import models



class Contacted(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=600)
    sender = models.EmailField()
    uuid = models.IntegerField('id' ,primary_key=True)
