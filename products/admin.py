from django.contrib import admin
from .models import Product
# Register your models here.

class ProductTable(admin.ModelAdmin):
    list_display =['name','price','stock','time']
admin.site.register(Product,ProductTable)