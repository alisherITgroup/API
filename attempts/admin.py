from django.contrib import admin
from .models import Attempt

@admin.register(Attempt)
class AttemptModelAdmin(admin.ModelAdmin):
    list_display = ["status", "problem", "author", "time"]
    list_filter = ["author", "problem"]
