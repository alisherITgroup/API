from rest_framework import serializers
from .models import Post, Tag, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "slug", "title", "body", "tags", "created_date", "updated_date")

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Post Tag"
        model = Tag
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Post Comment"
        model = Comment
        fields = "__all__"