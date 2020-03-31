from django.contrib import admin
from food.models import UserProfile, Restaurant, Comment
admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Comment)
