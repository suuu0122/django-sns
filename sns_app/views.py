from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, "sns_app/signup.html")
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
            return render(request, "sns_app/signin.html", {"error": "logged in"})
        else:
            return render(request, "sns_app/signin.html", {"error": "not logged in"})
    return render(request, "sns_app/signin.html", {"error": "get method"})