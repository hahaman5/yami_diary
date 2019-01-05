from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Idea,Division


admin.site.register(Idea)
admin.site.register(Division)
