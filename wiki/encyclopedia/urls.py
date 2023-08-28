from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.new_page, name="new_page"),
    path("entry/<str:name>", views.entry, name="entry"),
    path("random", views.random_entry, name="random"),
    path("search", views.search, name="search")
]
