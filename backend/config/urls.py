from django.contrib import admin
from django.urls import path, include
from user.views import getRoutes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("", getRoutes),
    path("otp/", include("otp.urls")),
]
