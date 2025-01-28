from django.urls import path

from . import views

# urls for product app
urlpatterns = [
    path("", views.home, name="home"),
    path("add_product/", views.add_product, name="add_product"),
]
