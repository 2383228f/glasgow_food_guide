from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]