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
    # GET: localhost:8000/user/
    path("", getRoutes),
    # POST: localhost:8000/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: localhost:8000/user/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    # POST: localhost:8000/user/reset/
    path(route="reset/", view=UserPasswordResetView.as_view(), name="password_reset"),
    # POST: localhost:8000/user/forgotten/
    path(
        route="forgotten/",
        view=ForgottenPasswordResetView.as_view(),
        name="password_forgotten",
    ),
    # PATCH: localhost:8000/user/profile/update/
    path(
        route="/profile/update/",
        view=UpdateProfileView.as_view(),
        name="update_profile",
    ),
    # localhost:8000/user/
    path("token/", include("user.token_api.urls")),
]
