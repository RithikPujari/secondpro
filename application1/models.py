from django.db import models

class Drug(models.Model):
    Did=models.IntegerField()
    Dname=models.CharField(max_length=25)
    Duse=models.CharField(max_length=25)
