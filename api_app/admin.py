from django.contrib import admin
from .models import SchoolModel
# Register your models here.


@admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
