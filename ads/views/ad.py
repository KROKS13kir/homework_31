from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, ListAPIView

from HW27.settings import TOTAL_ON_PAGE
from ads.models.ad import Ad
from ads.models.category import Category
from ads.serializers.ad import AdSerializer, AdImageSerializer, AdUpdateSerializer, AdCreateSerializer
from users.models import User


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.Get.getlist('cat', None)
        cat_query = None
        for category in categories:
            if cat_query is None:
                cat_query = Q(category__id__exact=category)
            else:
                cat_query |= Q(category__id__exact=category)
        if cat_query:
            self.queryset = self.queryset.filter(
                cat_query
            )

        advert_name = request.GET.get('text', None)
        if advert_name:
            self.queryset = self.queryset.filter(
                name__icontains=advert_name
            )

        user_location = request.GET.get('location', None)
        if user_location:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=user_location
            )

        price_from = request.GET.get('price_from', None)

        if price_from:
            self.queryset = self.queryset.filter(
                price__gte=price_from
            )
        price_to = request.GET.get('price_to', None)
        if price_to:
            self.queryset = self.queryset.filter(
                price__lte=price_to
            )
        return super().get(request, *args, **kwargs)

class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer

class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

