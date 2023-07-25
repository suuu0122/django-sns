from django.urls import path

from . import views



app_name = "sns_app"
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('list/', views.list_view, name="list"),
    path('logout/', views.logout_view, name="logout"),
    path('detail/<int:pk>', views.detail_view, name="detail"),
    path('good/<int:pk>', views.good, name="good"),
]