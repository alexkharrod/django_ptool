from django.urls import path

from . import views

# urls for quotes app
urlpatterns = [
    path("", views.home, name="home"),
    path("create-quote/", views.create_quote, name="create_quote"),
    path("quotes/", views.quotes, name="quotes"),
    path("view-quote/<int:pk>/", views.view_quote, name="view_quote"),
    path("quote/<int:quote_id>/pdf/", views.quote_pdf, name="quote_pdf"),
    path("edit-quote/<int:pk>/", views.edit_quote, name="edit_quote"),
]
