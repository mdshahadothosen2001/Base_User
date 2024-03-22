from django.urls import path, include
from .views import (
    UpdateProfileView,
)


urlpatterns = [
    # PATCH: localhost:8000/user/profile/update/
    path(
        route="profile/update/",
        view=UpdateProfileView.as_view(),
        name="update_profile",
    ),
    # localhost:8000/user/token/
    path("token/", include("user.token_api.urls")),
]
