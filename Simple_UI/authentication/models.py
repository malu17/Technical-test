from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, nombre, apellido, email, cedula,imagen_de_Perfil,pais,entidad, password=None):
        if nombre is None:
            raise TypeError('Users should have a name')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(nombre=nombre,apellido=apellido, email=self.normalize_email(email),cedula=cedula,imagen_de_Perfil=imagen_de_Perfil,pais=pais, entidad=entidad)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nombre, apellido, email, cedula,imagen_de_Perfil,pais,entidad, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(nombre, apellido, email, cedula,imagen_de_Perfil,pais, entidad, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = [
        ('EPS', 'EPS'),
        ('IPS', 'IPS'),
        ('ARL', 'ARL')
    ]


    nombre = models.CharField(max_length=255, unique=True, db_index=True)
    apellido = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    cedula = models.IntegerField()
    imagen_de_Perfil = models.FileField(upload_to='imagenes/', null=True, blank=True)
    pais = models.CharField(max_length=50)
    entidad = models.CharField(choices=CHOICES, max_length=50)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido','cedula', 'imagen_de_Perfil','pais', 'entidad']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
