from rest_framework import serializers


def check_not_published(value: bool):
    if value:
        raise serializers.ValidationError(f"Это поле не может быть True")