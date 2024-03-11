from django.urls import path
from . import views

app_name = "pay"

urlpatterns = [
    path("payment_success/", views.payment_success, name="payment_success"),
]
