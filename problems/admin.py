from django.contrib import admin
from .models import Problem, Tag, Language

@admin.register(Problem)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = ["slug", "name", "difficulty", "created_date", "updated_date"]
    list_editable = ["name", "difficulty"]
    list_filter = ["author", "type", "difficulty"]
    search_fields = ["name"]

@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ["command", "name"]

@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_date", "updated_date"]