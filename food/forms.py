from django import forms
from django.contrib.auth.models import User
from food.models import UserProfile, Restaurant, Comment
from datetime import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('is_owner', 'verified_by',)
        
class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text = "Please enter the restaurant name.")
    address = forms.CharField(max_length=100, help_text = "Please enter the restaurant address.", required=False)
    overview = forms.CharField(max_length=100, help_text = "Please enter a brief overview")
    detailed = forms.CharField(max_length=300, required=False, help_text = "Please enter a detailed description")
    phone_number = forms.IntegerField(required=False, help_text = "Please enter your phone number")
    email_address = forms.EmailField(required=False, help_text = "Please enter your email address")
    rating = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    price = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    owner = forms.ModelChoiceField(widget=forms.HiddenInput(),initial=UserProfile.objects.all().first(), queryset=UserProfile.objects.all())
    
    class Meta:
        model=Restaurant
        fields=('name', 'address', 'overview','detailed','phone_number','email_address',)
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=1000, help_text="Please write your comment here.")
    rating_choices =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"),
) 
    date_time = forms.DateTimeField(widget = forms.HiddenInput(), initial=datetime.now())
    rating = forms.ChoiceField(choices=rating_choices, help_text="rating")
    price_choices =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
) 
    restaurant = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Restaurant.objects.all(),required=False)
    price = forms.ChoiceField(choices=price_choices,help_text="price")
    
    class Meta:
        model = Comment
        fields =('comment','rating','restaurant','price')