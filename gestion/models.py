from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now=True)


class User(models.Model):
    username = models.CharField(max_length=250, unique= True)
    correo = models.CharField(max_length=250, unique= True)
    password = models.CharField(max_length= 128)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="usuarios")

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=250)