from django.db import models
from gestion.models import TipoCuenta, User

class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    edad = models.IntegerField()
    genero = models.CharField(max_length=24)
    sueldo = models.FloatField()
    trabajo = models.IntegerField()

class Cuenta(models.Model):
    monto = models.FloatField()
    numero = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)

class Credito(models.Model):
    cuotas = models.IntegerField()
    fecha = models.DateTimeField()
    monto = models.FloatField()
    pagado = models.BooleanField()
    tasa = models.FloatField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)