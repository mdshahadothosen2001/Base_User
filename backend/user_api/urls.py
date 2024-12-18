from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from user_api.views.register import UserRegistrationView
from user_api.views.activate import UserActivationView
from user_api.views.password_change import UserPasswordChangeView
from user_api.views.password_recover import UserPasswordRecoverView
from user_api.views.profile_update import UserProfileUpdateView
from user_api.views.token import CustomTokenObtainPairView
from user_api.views.otp import ResendOTPView


urlpatterns = [
    # POST: localhost:8091/user/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # POST: localhost:8091/user/account/otp/resend/
    path(route="account/otp/resend/", view=ResendOTPView.as_view(), name="otp_resend"),
    # POST: localhost:8091/user/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    # POST: localhost:8091/user/password/change/
    path(
        route="password/change/",
        view=UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    # POST: localhost:8091/user/password/recover/
    path(
        route="password/recover/",
        view=UserPasswordRecoverView.as_view(),
        name="password_recover",
    ),
    # PATCH: localhost:8091/user/profile/update/
    path(
        route="profile/update/",
        view=UserProfileUpdateView.as_view(),
        name="update_profile",
    ),
    # POST: localhost:8091/user/token/
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="token"),
    # POST: localhost:8091/user/token/refresh/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
]
