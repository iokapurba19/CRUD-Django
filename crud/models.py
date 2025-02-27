from django.db import models

# Create your models here.
class CRUD(models.Model):
    userid = models.CharField(max_length=4, primary_key=True, default='0000')
    username = models.CharField(max_length=10, default='default_username')
    password = models.CharField(max_length=10, default='default_password')