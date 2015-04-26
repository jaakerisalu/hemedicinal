# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    # Mostly copied from django.contrib.auth.models.UserManager

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_code = models.IntegerField('Isikukood', null=True, blank=True)
    address = models.CharField('Aadress', max_length=100, null=True, blank=True)
    first_name = models.CharField('Eesnimi', max_length=50, null=True, blank=True)
    last_name = models.CharField('Perekonnanimi', max_length=50, null=True, blank=True)
    phone = models.IntegerField('Telefoni nr', null=True, blank=True)
    email = models.EmailField('emaili aadress', max_length=254, unique=True)

    PROFESSION_APOTHECARY = 1
    PROFESSION_LOGISTIC = 2
    PROFESSION_OWNER = 3
    PROFESSION_CHOICES = (
        (PROFESSION_APOTHECARY, 'Apteeker'),
        (PROFESSION_LOGISTIC, 'Ravimihaldusjuht'),
        (PROFESSION_OWNER, 'Omanik'),
    )

    profession = models.PositiveSmallIntegerField(choices=PROFESSION_CHOICES, default=PROFESSION_APOTHECARY, null=True,
                                                  blank=True)

    STATUS_ACTIVE = 1
    STATUS_ON_HOLIDAY = 2
    STATUS_INACTIVE = 3
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Aktiivne'),
        (STATUS_ON_HOLIDAY, 'Puhkusel'),
        (STATUS_INACTIVE, 'Mitteaktiivne'),
    )

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_ACTIVE, null=True,
                                              blank=True)

    # Below is required by Django's UserAdmin
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.name
