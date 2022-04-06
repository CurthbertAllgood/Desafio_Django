from enum import auto
from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechanac = models.DateField(auto_now=True)
    
class prueba(models.Model):
    nombre=models.TextField(max_length=40)
    edad=models.IntegerField()
    