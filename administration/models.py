from django.db import models

# Create your models here.

class Alert(models.Model):
    mensaje = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=20, null=True)
    fecha = models.CharField(max_length=100, null=True)
   
    #triggered_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se activó la alarma")
    #active_boolean = models.BooleanField(default=True, help_text="Indica si la alarma está activa")

class Computer(models.Model):
    serial = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()  # 👈 Este debe ser un DateField
    previous_repairs = models.TextField(blank=True, null=True)