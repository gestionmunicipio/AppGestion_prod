from django.db import models

# Create your models here.

class Proceso(models.Model):
    unidad = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

class Evaluaciones(models.Model):
    id_proceso = models.IntegerField(default=0,blank=True)
    nro_pilar = models.SmallIntegerField(default=0,blank=True)
    p1 = models.SmallIntegerField(default=0,blank=True)
    p2 = models.SmallIntegerField(default=0,blank=True)
    p3 = models.SmallIntegerField(default=0,blank=True)
    p4 = models.SmallIntegerField(default=0,blank=True)
    p5 = models.SmallIntegerField(default=0,blank=True)
    p6 = models.SmallIntegerField(default=0,blank=True)
    p7 = models.SmallIntegerField(default=0,blank=True)
    p8 = models.SmallIntegerField(default=0,blank=True)
    p9 = models.SmallIntegerField(default=0,blank=True)
    p10 = models.SmallIntegerField(default=0,blank=True)

class Evaluacion(models.Model):
    id_proceso = models.IntegerField(default=0,blank=True)
    unidad = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    total_personas = models.SmallIntegerField(default=0,blank=True)
    total_cultura = models.SmallIntegerField(default=0,blank=True)
    total_liderazgo = models.SmallIntegerField(default=0,blank=True)
    total_estrategia = models.SmallIntegerField(default=0,blank=True)
    total_estructura = models.SmallIntegerField(default=0,blank=True)
    total_operaciones = models.SmallIntegerField(default=0,blank=True)
    total_creatividad = models.SmallIntegerField(default=0,blank=True)
    total_tecnologia =  models.SmallIntegerField(default=0,blank=True)
