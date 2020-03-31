from django.urls import path
from food import views
from food.views import show_restaurant

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('add_restaurant/', views.add_restaurant, name = 'add_restaurant'),
    path('restaurant/<slug:restaurant_name_slug>/add_comment/', views.add_comment, name='add_comment'),
    path('restaurant/<slug:restaurant_name_slug>/',views.show_restaurant, name='show_restaurant'),

]