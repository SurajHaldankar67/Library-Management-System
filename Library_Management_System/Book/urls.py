from django.urls import path
from .views import add_book, get_book_data, view_all_book

urlpatterns = [
    path("add_book", add_book, name="add_book"),
    path("get_book", get_book_data, name="get_book_info"),
    path("view_all_book", view_all_book, name="view_all_book"),
]

