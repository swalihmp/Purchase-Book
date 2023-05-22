from django.contrib import admin
from . models import products,user_data,short

# Register your models here.

admin.site.register(user_data),
admin.site.register(products),
admin.site.register(short),