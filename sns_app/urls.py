from django.urls import path

from . import views



app_name = "sns_app"
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('list/', views.list_view, name="list"),
]