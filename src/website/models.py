# Register your models here
from django.db import models



class Contacted(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField()
    sender = models.EmailField()
    uuid = models.UUIDField('id')
    
    class Meta:
      app_label = 'Contact_me_MSG'
      db_table = 'contactme'
      abstract = False