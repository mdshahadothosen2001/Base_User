from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserActivationView,
)


urlpatterns = [
    # POST: 127.0.0.1:8000/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: 127.0.0.1:8000/user/activate/
    path(
        route="activate/", view=UserActivationView.as_view(), name="user_activation"
    ),

]