from rest_framework.viewsets import ModelViewSet

from ads.models.category import Category
from ads.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Viewset for category model"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer