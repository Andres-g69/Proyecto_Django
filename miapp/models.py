from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key= True, max_length=5)
    cli_nombre = models.CharField(max_length=40, null=True, blank=True)
    cli_direccion = models.CharField(max_length=60, null=True, blank=True)
    cli_telefono = models.CharField(max_length=24, null=True, blank=True)
    cli_mail = models.CharField(max_length=60, null=True, blank=True)

class Meta:
    db_table ='CLIENTE'

def __str__(self):
    return self.cli_nombre or f"Cliente{self.id_cliente}"

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, to_field='id_cliente')
    ord_fecha = models.DateField(null=True, blank=True)

class Meta:
    db_table= 'ORDEN'

def __str__(self):
    return f"Orden{self.id_orden}"

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key= True, max_length=10, null=True, blank=True)
    emp_nombre = models.CharField(max_length=20, null=True, blank=True)
    emp_apellido = models.CharField(max_length=20, null=True, blank=True)
    emp_titulo = models.CharField(max_length=30, null=True, blank=True)
    emp_mail = models.CharField(max_length=25, null=True, blank=True)
    emp_fechanac = models.DateField(null=True, blank=True)
    emp_fecha_contrato = models.DateField(null=True, blank=True)
    emp_direccion = models.CharField(max_length=60, null=True, blank=True)
    #emp_foto = models.blob()

class Meta:
    db_table= 'EMPLEADO'

def __str__(self):
    return f"Empleado{self.id_empleado}"

class Detalle_Orden(models.Model):
    id_detord = models.AutoField(primary_key=True, max_length=10, null=True, blank=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, to_field='id_producto')
    deo_precio = models.FloatField(max_length=20, null=True, blank=True)
    deo_cantidad = models.IntegerField(max_length=5, null=True, blank=True)

class Meta:
    db_table= 'DETALLE_ORDEN'

def __str__(self):
    return f"Detalle_Orden{self.id_detord}"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, null=True, blank=True)