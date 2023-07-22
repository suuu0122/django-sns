from django.shortcuts import render



def signup(request):
    return render(request, "sns_app/signup.html", {})