from django.urls import path

from . import views

# urls for product app
urlpatterns = [
    path("", views.products, name="products"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit/<int:pk>/", views.edit_product, name="edit_product"),
    path("view/<int:pk>/", views.view_product, name="view_product"),
    path("npds/<int:product_id>/pdf/", views.npds, name="npds"),
]
