from django.contrib import admin
from .models import Post, Tag, Comment

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date", "updated_date"]

@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_date", "updated_date"]

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["reply_id", "author", "created_date", "updated_date"]
