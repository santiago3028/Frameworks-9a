from django.db import models

# Create your models here.
class paises(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=180, )
    nombre=models.CharField(max_length=180)
    abreviatura=models.CharField(max_length=80)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class ciudades(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=180, )
    nombre=models.CharField(max_length=180)
    abreviatura=models.CharField(max_length=80)
    id_pais=models.ForeignKey(paises, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class afiliados(models.Model):
    id=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=180, )
    apellidos=models.CharField(max_length=180)
    movil=models.IntegerField()
    direccion=models.CharField(max_length=280)
    email=models.EmailField(unique=True)
    id_ciudad=models.ForeignKey(ciudades, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()