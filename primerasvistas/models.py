from django.db import models

# Create your models here.

class familiar(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)