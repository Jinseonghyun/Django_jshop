from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


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


def category_summary(requset):
    categories = Category.objects.all()
    return render(requset, "store/category_summary.html", {"categories": categories})


def search(requset):
    if requset.method == "POST":
        searched = requset.POST["searched"]
        searched = Product.objects.filter(
            Q(name__icontains=searched) | Q(desciption__icontains=searched)
        )
        if not searched:
            messages.success(requset, ("상품이 존재하지 않습니다."))
            return render(requset, "store/search.html", {})
        else:
            return render(requset, "store/search.html", {"searched": searched})
    else:
        return render(requset, "store/search.html", {})
