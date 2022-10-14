from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ads.models.selection import Selection


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'

class SelectionCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'