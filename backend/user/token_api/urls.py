from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import (
    MyTokenObtainPairView,
    home_view,
)


urlpatterns = [
    # POST: localhost:8000/user/token/
    path(
        route="", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    # POST: localhost:8000/user/token/refresh/
    path(route="refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GET: localhost:8000/user/token/home/
    path(route="home/", view=home_view.as_view(), name="home"),
]
