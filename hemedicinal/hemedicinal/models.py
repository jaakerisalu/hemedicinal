from django.db import models
from accounts.models import User


class Supplier(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 2
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Aktiivne'),
        (STATUS_INACTIVE, 'Mitteaktiivne'),
    )

    name = models.CharField('Tarnija nimi', max_length=50, unique=True)
    address = models.CharField('Tarnija Aadress', max_length=100)
    phone = models.IntegerField('Telefoni nr')
    email = models.CharField('Email', max_length=100)
    status = models.PositiveSmallIntegerField('Seisund', choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField('Tootja nimi', max_length=50, unique=True)
    description = models.CharField('Tootja kirjelus', max_length=100)

    def __str__(self):
        return self.name


class Substance(models.Model):
    name = models.CharField('Mõjuaine nimi', max_length=50, unique=True)
    atc_code = models.CharField('ATC kood', max_length=7)
    description = models.CharField('Mõjuaine kirjelus', max_length=100)

    def __str__(self):
        return self.name


class Drug(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 2
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Aktiivne'),
        (STATUS_INACTIVE, 'Mitteaktiivne'),
    )

    name = models.CharField('Ravimi nimi', max_length=50, unique=True)
    price = models.DecimalField('Ravimi hind', decimal_places=2, max_digits=10)
    description = models.CharField('Ravimi kirjeldus', max_length=255)
    status = models.PositiveSmallIntegerField('Seisund', choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    supplier = models.ForeignKey(Supplier, verbose_name="Tarnija")
    substance = models.ForeignKey(Substance, verbose_name="Mõjuaine")
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Tootja")
    creator = models.ForeignKey(User, verbose_name="Töötaja", related_name="created_drugs")

    def __str__(self):
        return self.name
