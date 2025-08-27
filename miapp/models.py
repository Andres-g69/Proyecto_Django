from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key= True, max_length=5)
    cli_nombre = models.CharField(max_length=40, null=True, blank=True)
    cli_direccion = models.CharField(max_length=60, null=True, blank=True)
    cli_telefono = models.CharField(max_length=24, null=True, blank=True)
    cli_mail = models.CharField(max_length=60, null=True, blank=True)
    
class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, to_field='id_cliente')
    ord_fecha = models.DateField(null=True, blank=True)

    
