from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django import forms
from .models import Profile
import json
from cart.cart import Cart


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

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
            return redirect("accounts:update_info")
        else:
            messages.success(request, ("회원가입에 실패했습니다. 다시 시도해주세요."))
            return redirect("accounts:register")
    else:
        return render(request, "accounts/register.html", {"form": form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "프로필이 변경되었습니다.")
            return redirect("store:home")
        return render(request, "accounts/update_user.html", {"user_form": user_form})

    else:
        messages.success(request, "로그인 후 다시 시도해주세요. ")
        return redirect("store:home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "고객님의 비밀번호가 변경되었습니다.")
                return redirect("accounts:update_password")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("accounts:update_password")

        else:
            form = ChangePasswordForm(current_user)
            return render(request, "accounts/update_password.html", {"form": form})
    else:
        messages.success(request, "로그인 후 다시 시도해주세요. ")
        return redirect("store:home")


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)

        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()

            messages.success(request, "프로필 정보가 변경되었습니다.")
            return redirect("store:home")
        return render(
            request,
            "accounts/update_info.html",
            {"form": form, "shipping_form": shipping_form},
        )

    else:
        messages.success(request, "로그인 후 다시 시도해주세요. ")
        return redirect("store:home")
