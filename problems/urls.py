from django.urls import path
from .views import like, unlike, buy, buy_cases
from rest_framework.routers import DefaultRouter
from .viewsets import ProblemViewSet, TagViewSet, LanguageViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'all', ProblemViewSet)
router.register(r'tags', TagViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("all/<int:pk>/like/", like, name="like_problem"),
    path("all/<int:pk>/unlike/", unlike, name="unlike_problem"),
    path("all/<int:pk>/buy/", buy, name="buy_problem"),
    path("all/<int:pk>/buy_cases/", buy_cases, name="buycases_problem"),
]

urlpatterns += router.urls