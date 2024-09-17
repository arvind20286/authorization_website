from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("verify/", views.verify, name="verify"),
    path("logout/", views.logout, name="logout"),
    path("google-signin/", views.googleSignin, name="google-signin"),
    path("welcome/", views.welcome, name='welcome')
]