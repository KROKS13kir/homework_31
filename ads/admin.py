from django.contrib import admin

# Register your models here.
from ads.models.ad import Ad
from ads.models.category import Category
from ads.models.location import Location

admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Location)
