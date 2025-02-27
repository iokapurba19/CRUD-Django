from django.db import models

# Create your models here.
class CRUD(models.Model):
    userid = models.CharField(max_length=4, default=0)
    username = models.CharField(max_length=10, default='guest') 
    password = models.CharField(max_length=255, default='defaultpassword')