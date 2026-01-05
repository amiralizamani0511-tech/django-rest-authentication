from django.contrib import admin
from .models import Kala

class Manageadmin(admin.ModelAdmin):
    list_display = ["name","price","status"]




admin.site.register(Kala,Manageadmin)
