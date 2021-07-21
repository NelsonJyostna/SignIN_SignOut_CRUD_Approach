from django.db import models

# Create your models here.
class Student(models.Model):
    rn=models.IntegerField()
    name=models.CharField(max_length=20)
    marks=models.FloatField()
    city=models.CharField(max_length=20)
    Dist=models.CharField(max_length=20, null=True)