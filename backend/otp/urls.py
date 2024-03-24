from django.urls import path

from .views import ResentOTPView


urlpatterns = [
    # POST: 127.0.0.1:8091/otp/resend/
    path(route="resend/", view=ResentOTPView.as_view(), name="otp_resend"),
]
