from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserActivationView,
    UserPasswordResetView,
    ForgottenPasswordResetView,
    UpdateProfileView,
)


urlpatterns = [
    # POST: localhost:8000/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: localhost:8000/user/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    # POST: localhost:8000/user/password/reset/
    path(
        route="password/reset/",
        view=UserPasswordResetView.as_view(),
        name="password_reset",
    ),
    # POST: localhost:8000/user/password/forgotten/
    path(
        route="password/forgotten/",
        view=ForgottenPasswordResetView.as_view(),
        name="password_forgotten",
    ),
    # PATCH: localhost:8000/user/profile/update/
    path(
        route="profile/update/",
        view=UpdateProfileView.as_view(),
        name="update_profile",
    ),
    # localhost:8000/user/token/
    path("token/", include("user.token_api.urls")),
]
