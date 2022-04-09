from django.urls import path
from .views import Student_registration_form, student_login_form, student_logout_view, student_section
urlpatterns = [

    path("registation_form", Student_registration_form, name="student_registration_form"),
    path("student_login", student_login_form, name="student_login_form"),
    path("student_logout", student_logout_view, name="student_logout"),
    path("student_section", student_section, name="student_section"),

]

