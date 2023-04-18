from rest_framework.viewsets import ModelViewSet
from .serializer import ProblemSerializer, LanguageSerializer, TagSerializer, CommentSerializer
from .models import Problem, Language, Tag, Comment
from django_filters import rest_framework

class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    # filterset_fields = ['author']
    search_fields = ["name"]

    def filter_queryset(self, queryset):
        if self.request.GET.get("search"):
            queryset = Problem.objects.all().filter(name__icontains=self.request.GET.get("search"))
        if self.request.GET.get("tag"):
            tag = Tag.objects.all().filter(name__icontains=self.request.GET.get("tag")).first()
            queryset = Problem.objects.all().filter(tags__in=[tag.pk])
        if self.request.GET.get("type"):
            queryset = Problem.objects.all().filter(type__icontains=self.request.GET.get("type"))
        return super().filter_queryset(queryset)

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer