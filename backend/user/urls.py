from django.urls import path, include


urlpatterns = [
    # localhost:8000/user/token/
    path("token/", include("user.token_api.urls")),
]
