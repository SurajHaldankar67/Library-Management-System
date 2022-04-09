from django.shortcuts import render, redirect
from .forms import Login_form
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def Student_registration_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('Student:student_login_form')
    else:
        form = UserCreationForm()
    return render(request, 'student_registration_form.html', {'form': form})

def student_login_form(request):
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
                return redirect("Student:student_section")

        else:
            form = Login_form()
    return render(request, "student_login_form.html", context={"form": form})

def student_section(request):

    return render(request, "student_section.html")

def student_logout_view(request):
    if request.method == 'POST':
            logout(request)
    return redirect("/")

