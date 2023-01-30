from django.contrib import admin
from .models import Category, Dishes

admin.site.register(Category)

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_filter = ('category', 'position', )
    list_display = ['name', 'position', 'is_visible', 'price', 'photo', 'category']
    list_editable = ['position', 'is_visible', 'price']
    prepopulated_fields = {'slug': ('name', ), }
