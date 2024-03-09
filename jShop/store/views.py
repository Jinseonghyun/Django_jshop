from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


def about(request):
    return render(request, "store/about.html", {})


def product(requset, pk):
    product = Product.objects.get(id=pk)
    return render(requset, "store/product.html", {"product": product})


def category(requset, s):
    try:
        category = Category.objects.get(name=s)
        products = Product.objects.filter(category=category)
        return render(
            requset, "store/category.html", {"products": products, "category": category}
        )
    except:
        messages.success(requset, ("카테고리가 존재하지 않습니다."))
        return redirect("store/home.html")
