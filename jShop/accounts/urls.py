from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("update_user/", views.update_user, name="update_user"),
    path("update_password/", views.update_password, name="update_password"),
    path("update_info/", views.update_info, name="update_info"),
]
