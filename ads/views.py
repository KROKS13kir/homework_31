import json

from django.http.response import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.detail import DetailView

from ads.models import Ad, Category


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):

    def get(self, request):
        advertisements = Ad.objects.all()

        response = [{
            "id": ad.id,
            "author": ad.author,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }
            for ad in advertisements
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        advert_body = json.loads(request.body)
        ad = Ad.objects.create(**advert_body)

        response = {
            "id": ad.id,
            "author": ad.author,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})

class AdDetailView(DetailView):
    model = Ad

    def get(self, *args, **kwargs):

        advertisement = self.get_object()

        response = {
            "id": advertisement.id,
            "author": advertisement.author,
            "name": advertisement.name,
            "price": advertisement.price,
            "description": advertisement.description,
            "address": advertisement.address,
            "is_published": advertisement.is_published
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):

    def get(self, request):
        categories = Category.objects.all()

        response = [{
            "id": cat.id,
            "name": cat.name,
        }
            for cat in categories
        ]

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_body = json.loads(request.body)
        cat = Category.objects.create(**category_body)

        response = {
            "id": cat.id,
            "name": cat.name,
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        category = self.get_object()

        response = {
            "id": category.id,
            "name": category.name,
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
