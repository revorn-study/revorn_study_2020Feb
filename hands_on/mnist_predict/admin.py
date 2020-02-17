from django.contrib import admin
from .models import PredictNumber


@admin.register(PredictNumber)
class PredictNumberAdmin(admin.ModelAdmin):
    pass