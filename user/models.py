from django.db import models

class PersonBase(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='authorized_personnel/')

    class Meta:
        abstract = True

class AuthorizedPersonnel(PersonBase):
    # hereda nombre y foto
    # si ya tenías campos adicionales, los mantienes aquí
    def __str__(self):
        return self.nombre
