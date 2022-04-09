from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import Login_form
from django.contrib import messages

# Create your views here.


def administrator_login_page(request):
    form = Login_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            check_user = authenticate(username=user, password=passw)
            print(user)
            context = {"username": user}
            if check_user is not None:
                messages.success(request, context)
                login(request, check_user)
                return redirect("administrator:administrator_section")

        else:
            form = Login_form()
    return render(request, "administrator_login.html", context={"form": form})

def administrator_section(request):

    return render(request, "administrator_section.html")

def logout_view(request):
    if request.method == 'POST':
            logout(request)
    return redirect("/")