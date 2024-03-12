from django.urls import path
from .views.register import UserRegistrationView


urlpatterns = [
    # POST: localhost:8091/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
]
