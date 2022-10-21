import factory
from factory.django import DjangoModelFactory

from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'test_password'