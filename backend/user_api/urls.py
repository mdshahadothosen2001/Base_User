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
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    path(route="account/otp/resend/", view=ResendOTPView.as_view(), name="otp_resend"),
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    path(
        route="password/change/",
        view=UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        route="password/recover/",
        view=UserPasswordRecoverView.as_view(),
        name="password_recover",
    ),
    path(
        route="profile/update/",
        view=UserProfileUpdateView.as_view(),
        name="update_profile",
    ),
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="token"),
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
]
