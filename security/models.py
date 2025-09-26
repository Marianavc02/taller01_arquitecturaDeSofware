from django.db import models

class Fotografia(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Fotografía {self.id}"


