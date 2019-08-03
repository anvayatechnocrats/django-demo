from django.urls import path
from basic_app.views import base, index, user_logout, user_login, registration

app_name = "basic_app"

urlpatterns = [
    path("index/", index, name="index" ),
    path("base/", base, name="base" ),
    path("user_login/", user_login, name="user_login" ),
    path("user_logout/", user_logout, name="user_logout" ),
    path("registration/", registration, name="registration" ),
]
