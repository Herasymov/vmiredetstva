from django.contrib import admin
from ecomapp.models import Category
from ecomapp.models import Brand
from ecomapp.models import Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
