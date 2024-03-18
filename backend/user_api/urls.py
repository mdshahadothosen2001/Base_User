from django.urls import path

from .views.register import UserRegistrationView
from .views.activate import UserActivationView


urlpatterns = [
    # POST: localhost:8091/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: localhost:8091/user/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
]
