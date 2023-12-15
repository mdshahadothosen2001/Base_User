from django.urls import path, include
from .views import (
    UserRegistrationView,
)


urlpatterns = [
    # POST: 127.0.0.1:8000/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),

]