from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AlgorithmsHubOpenAPI",
        description="Algorithmshub tizimining ochiq manbali API i",
        default_version="1.0.0",
        contact=openapi.Contact(
            name="Ali",
            url="https://algorithmshub.uz",
            email="ali@algorithmshub.uz"
        )
    ),
    public=True,
    permission_classes= (permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('problems/', include('problems.urls')),
    path('attempts/', include('attempts.urls')),
    path('posts/', include('posts.urls')),
    path('', include('home.urls')),
    path("doc/", schema_view.with_ui(
        "swagger", cache_timeout=0
    ), name="swagger"),
]
