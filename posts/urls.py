from django.urls import path
from .viewsets import PostViewSet, TagViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("all", PostViewSet)
router.register("tags", TagViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [

]

urlpatterns += router.urls