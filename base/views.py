from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.


def loginPage(request):
    page = "login"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "base/login_reg.html", {"page": page})


def logoutuser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def Home(request):
    return render(request, "base/home.html")
    return render(request, "base/home.html")


def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                request, username=user.username, password=request.POST["password1"]
            )

            if user is not None:
                login(request, user)
                return redirect("home")

    context = {"form": form, "page": page}
    return render(request, "base/login_reg.html", context)
    return render(request, "base/login_reg.html", context)
    return render(request, "base/login_reg.html", context)
    return render(request, "base/login_reg.html", context)
