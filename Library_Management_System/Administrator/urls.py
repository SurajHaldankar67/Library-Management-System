from django.urls import path
from .views import administrator_login_page, administrator_section, logout_view
urlpatterns = [
    path("login", administrator_login_page, name="administrator_login" ),
    path("administrator_section", administrator_section, name="administrator_section"),
    path("logout", logout_view, name="logout"),
]