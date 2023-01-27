from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    contactno = models.CharField(max_length=10)