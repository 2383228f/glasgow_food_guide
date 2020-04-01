from django.urls import path
from food import views


app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('add_restaurant/', views.add_restaurant, name = 'add_restaurant'),
    path('restaurants/<slug:restaurant_name_slug>/add_comment/', views.add_comment, name='add_comment'),
    path('restaurants/<slug:restaurant_name_slug>/',views.show_restaurant, name='show_restaurant'),
    path('restaurants/',views.show_restaurants, name='show_restaurants'),
    path('search/',views.search,name='search'),
    #path('account/',views.account,name='account'),
    path('account/',views.add_favourite,name='add_favourite'),

]