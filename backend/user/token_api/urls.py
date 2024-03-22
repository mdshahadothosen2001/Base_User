from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


urlpatterns = [
    # POST: localhost:8000/user/token/refresh/
    path(route="refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
]
