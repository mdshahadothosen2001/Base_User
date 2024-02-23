from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserActivationView,
    UserPasswordResetView,
    ForgottenPasswordResetView,
    UpdateProfileView,
    getRoutes,
)


urlpatterns = [
    path("test/", getRoutes),
    # POST: 127.0.0.1:8000/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: 127.0.0.1:8000/user/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    # POST: 127.0.0.1:8000/user//
    path(route="reset/", view=UserPasswordResetView.as_view(), name="password_reset"),
    # POST: 127.0.0.1:8000/user/forgotten/
    path(
        route="forgotten/",
        view=ForgottenPasswordResetView.as_view(),
        name="password_forgotten",
    ),
    # POST: 127.0.0.1:8000/user/update-profile/
    path(
        route="update-profile/",
        view=UpdateProfileView.as_view(),
        name="update-profile",
    ),
    path("", include("user.token_api.urls")),
]
