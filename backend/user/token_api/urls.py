from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import (
    MyTokenObtainPairView,
    UserTokenLoginView,
)


urlpatterns = [
    # POST: localhost:8000/user/token/
    path(
        route="", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    # POST: localhost:8000/user/token/refresh/
    path(route="refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GET: localhost:8000/user/token/login/
    path(route="login/", view=UserTokenLoginView.as_view(), name="token_login"),
]
