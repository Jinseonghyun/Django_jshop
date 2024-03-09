from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("로그인에 성공했습니다. "))
            return redirect("store:home")
        else:
            messages.success(request, ("로그인에 실패했습니다 , 다시 입력해주세요."))
            return redirect("accounts:login")
    else:
        return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, ("로그아웃 되었습니다. 다음에 또 방문해주세요 "))
    return redirect("store:home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("제이샵 회원으로 오신 것을 환영합니다.!!!"))
            return redirect("store:home")
        else:
            messages.success(request, ("회원가입에 실패했습니다. 다시 시도해주세요."))
            return redirect("accounts:register")
    else:
        return render(request, "accounts/register.html", {"form": form})
