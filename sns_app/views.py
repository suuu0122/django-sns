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



@login_required
def good_btn(rquest, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.good += 1
    tweet.save()
    return redirect("sns_app:list")



@login_required
def read_btn(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    username = request.user.get_username()
    if username in tweet.read_text:
        return redirect("sns_app:list")
    else:
        tweet.read += 1
        tweet.read_text = tweet.read_text + ' ' + username
        tweet.save()
        return redirect("sns_app:list")



@login_required
def create_view(request):
    if request.method == "POST":
        title       = request.POST["title"]
        content     = request.POST["content"]
        contributor = request.user.get_username()
        sns_image   = request.FILES["sns_image"]
        good        = 0
        read        = 0
        read_text   = contributor
        print(0)
        
        tweet = Tweet.objects.create(title=title, content=content, contributor=contributor, \
                                     sns_image=sns_image, good=good, read=read, read_text=read_text)
        print(0)
        return redirect("sns_app:list")
    return render(request, "sns_app/create.html")