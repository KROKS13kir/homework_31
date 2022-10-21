from factory.django import DjangoModelFactory
import factory
from ads.models.ad import Ad
from .category import CategoryFactory
from .user import UserFactory


class AdFactory(DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Test 10 characters minimum"
    price = 1000

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)