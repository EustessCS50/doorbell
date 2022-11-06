from django.contrib import admin
from . models import Meal, Categorie, Vendor, Customer


# Register your models here.

admin.site.register(Categorie)
admin.site.register(Vendor)
admin.site.register(Meal)
admin.site.register(Customer)
