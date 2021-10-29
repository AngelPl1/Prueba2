from django.db import models

# Create your models here.


class Categorias(models.Model):
    nombre = models.Charfield(verbose_name='Nombre de la pelicula', max_lenght=50)
    descripción = models.Charfield(verbose_name='Descripción resumida', max_lenght=150)
    Clasificaciones_de_edad = models.Charfield(verbose_name='A,B,B-15,C,D', max_lenght=30)

    def __str__(self):
        return self.nombre + ' ' + self.descripción + " " + self.edad + " "