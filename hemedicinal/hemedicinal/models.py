from django.db import models


class Supplier(models.Model):
    name = models.CharField('Ravimi nimi', max_length=255)

    def __str__(self):
        return self.name


class Drug(models.Model):
    name = models.CharField('Ravimi nimi', max_length=255)
    description = models.CharField('Ravimi kirjeldus', max_length=255)
    price = models.FloatField('Ravimi hind')
    supplier = models.ForeignKey(Supplier, verbose_name="Tarnija")

    def __str__(self):
        return self.name
