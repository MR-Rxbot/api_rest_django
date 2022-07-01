from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    precio=models.CharField(max_length=30)