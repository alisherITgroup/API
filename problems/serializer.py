from rest_framework import serializers
from .models import Problem, Language, Tag, Comment

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ("id", "author", "slug", "name", "problem", "timelimit", "memorylimit", "difficulty", "price", "infoin", "infoout", "comment","simpletests", "tests", "is_interactive", "solution", "created_date", "updated_date", "count", "count_likes", "count_unlikes", "count_buyers", "count_casebuyers", "count_solvers", "count_errors", "created_date", "updated_date", "likes", "unlikes", "buyers", "casebuyers", "solvers", "errors")

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Problem Tag"
        model = Tag
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Problem Comment"
        model = Comment
        fields = "__all__"