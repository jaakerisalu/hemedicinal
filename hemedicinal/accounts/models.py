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

class Tootaja(models.Model):
    class Meta:
        managed = False
        db_table = 'tootaja'

    tootaja_kood = models.AutoField(primary_key=True)

class User(AbstractBaseUser, PermissionsMixin):
    # Blank and null because I shouldn't add a default here
    tootaja = models.OneToOneField(Tootaja, blank=True, null=True)

    # Below is required by Django's UserAdmin
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, unique=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.name

