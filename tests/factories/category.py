import factory
from factory.django import DjangoModelFactory

from ads.models.category import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')