from django.urls import path

from . import views

# urls for product app
urlpatterns = [
    path("", views.home, name="home"),
]
