from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Camada: {self.camada}"

    
    
class Alumnos(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    curso = models.CharField(max_length=40)
    email = models.EmailField()
    apellido = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Camada: {self.camada} / Curso: {self.curso} / Email: {self.email} / Apellido: {self.apellido}"

    
class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()
    curso = models.CharField(max_length=40)
    