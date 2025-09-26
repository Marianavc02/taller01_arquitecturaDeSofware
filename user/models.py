from django.db import models

class AuthorizedPersonnel(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='authorized_personnel/')

    def __str__(self):
        return self.nombre
    