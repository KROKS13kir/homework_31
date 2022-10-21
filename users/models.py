import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from ads.models.location import Location


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор')
    )


class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=13)
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(limit_value=9, message='Allowed age 9 and over')]
    )
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username