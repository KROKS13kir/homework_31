from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView



from HW27.settings import TOTAL_ON_PAGE
from ads.models.ad import Ad
from ads.models.category import Category
from users.models import User


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list.select_related('author').select_related('category').order_by('-price')

        paginator = Paginator(ads, TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        ads_on_page = paginator.get_page(page_number)

        response = {
            "items": [
                {
                    'id': ad.id,
                    'author_id': ad.author_id,
                    'author': str(ad.author),
                    'name': ad.name,
                    'price': ad.price,
                    'description': ad.description,
                    'is_published': ad.is_published,
                    'image': ad.image.url if ad.image else None,
                    'category_id': ad.category_id,
                    'category': str(ad.category)
                } for ad in ads_on_page],
            "total": paginator.count,
            "number_of_pages": paginator.num_pages
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Category
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(
            name=ad_data.get('name'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            is_published=ad_data.get('is_published')
        )

        ad.author = get_object_or_404(User, pk=ad_data.get('author_id'))
        ad.category = get_object_or_404(Category, pk=ad_data.get('category_id'))
        ad.save()

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'category']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        ad = self.object

        ad.name = ad_data.get('name')
        ad.price = ad_data.get('price')
        ad.description = ad_data.get('description')
        ad.is_published = ad_data.get('is_published')
        ad.category_id = ad_data.get('category_id')

        ad.save()

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.image = request.FILES['image']
        ad.save()

        response = {
            'id': ad.id,
            'author_id': ad.author_id,
            'author': str(ad.author),
            'name': ad.name,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
            'image': ad.image.url if ad.image else None,
            'category_id': ad.category_id,
            'category': str(ad.category)
        }

        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'OK'},
                            status=200)
