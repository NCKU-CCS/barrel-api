from django.contrib import admin

# Register your models here.

from .models import Bucket


admin.site.register(Bucket)