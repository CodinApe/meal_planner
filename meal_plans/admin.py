from django.contrib import admin

# Register your models here.

from .models import Plan, FoodItem

admin.site.register(Plan)
admin.site.register(FoodItem)
