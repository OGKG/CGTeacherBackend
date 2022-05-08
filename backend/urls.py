from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    re_path(r"^auth/", include("djoser.urls.base")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
