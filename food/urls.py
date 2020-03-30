from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('add_restaurant/', views.add_restaurant, name = 'add_restaurant')
]