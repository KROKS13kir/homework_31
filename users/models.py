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
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True, unique=True)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=15)
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(limit_value=9, message='Allowed age 9 and over')]
    )
    birth_date = models.DateField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username