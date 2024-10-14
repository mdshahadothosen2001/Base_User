from django.urls import path

from .views import ResendOTPView


urlpatterns = [
    # POST: 127.0.0.1:8091/otp/resend/
    path(route="resend/", view=ResendOTPView.as_view(), name="otp_resend"),
]
