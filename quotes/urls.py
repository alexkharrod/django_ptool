from django.urls import path

from . import views

# urls for quotes app
urlpatterns = [
    path("", views.home, name="home"),
]
