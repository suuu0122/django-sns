from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            return render(request, "sns_app/signup.html")
        except IntegrityError:
            return render(request, "sns_app/signup.html", {"error": "このユーザはすでに登録されています"})
    return render(request, "sns_app/signup.html")