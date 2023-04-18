from rest_framework.viewsets import ModelViewSet
from .models import Post, Tag, Comment
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, TagSerializer, CommentSerializer

class PostPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 50
    max_page_size = 50

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def filter_queryset(self, queryset):
        if self.request.GET.get("search"):
            queryset = Post.objects.all().filter(title__icontains=self.request.GET.get("search"))
        if self.request.GET.get("tag"):
            tag = Tag.objects.all().filter(name__icontains=self.request.GET.get("tag")).first()
            queryset = Post.objects.all().filter(tags__in=[tag.pk])
        return super().filter_queryset(queryset)

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer