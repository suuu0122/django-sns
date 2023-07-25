from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from .models import Tweet



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, '', password)
            return redirect("sns_app:signin")
        except IntegrityError:
            return render(request, "sns_app/signup.html", {"error": "このユーザはすでに登録されています"})
    return render(request, "sns_app/signup.html")



def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("sns_app:list")
        else:
            return render(request, "sns_app/signin.html", {"error": "ユーザ名とパスワード名が正しくありません"})
    return render(request, "sns_app/signin.html", {})



@login_required
def list_view(request):
    tweets = Tweet.objects.all()
    return render(request, "sns_app/list.html", {"tweets": tweets})



@login_required
def logout_view(request):
    logout(request)
    return redirect("sns_app:signin")



@login_required
def detail_view(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, "sns_app/detail.html", {"tweet": tweet})