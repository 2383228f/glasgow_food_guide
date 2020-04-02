import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','glasgow_food_guide.settings')

from django.template.defaultfilters import slugify
from datetime import datetime
import django

django.setup()

from django.contrib.auth.models import User
from food.models import UserProfile, Restaurant, Comment
def populate():
    #First, we will create lists of dictionaries containing the pages
    #we want to add into each category.
    #Then we will create a dictionary of dictionaries for out categories.
    #This might seem a little bit confusing, but it allows us to iterate
    #through each data structure, and add the data to our models. 
    if not User.objects.filter(username="admin").exists():
        user0 = User.objects.create_superuser(username="admin", email="admin@gfg.com",password="temp")
        user0.set_password("pass")
        user0.save()
        userP0 = UserProfile.objects.get_or_create(user=user0,username=user0.username,is_owner=True)[0]
        
    user1 = User.objects.get_or_create(username="JoePizza",email="joe@gmail.com",password="password")[0]
    userP1 = UserProfile.objects.get_or_create(user=user1,username=user1.username,is_owner=True)[0]
    user1.set_password("password")
    user1.save()
    
    user2 = User.objects.get_or_create(username="Jane10",email="jane10@gmail.com",password="password")[0]
    userP2 = UserProfile.objects.get_or_create(user=user2,username=user2.username,is_owner=False)[0]
    user2.set_password("password")
    user2.save()
    
    user3 = User.objects.get_or_create(username="Jackie1234",email="jackie1234@gmail.com",password="password")[0]
    userP3 = UserProfile.objects.get_or_create(user=user3,username=user3.username,is_owner=False)[0]
    user3.set_password("password")
    user3.save()
    
    name = "Joes Pizza"
    rest1 = Restaurant.objects.get_or_create(owner=userP1,name="Joes Pizza",slug=slugify(name))[0]
    rest1.address = "8 Byres Road"
    rest1.overview = "Delicious Pizza"
    rest1.detailed = "Traditional pizza place that relies on traditional values"
    rest1.phone_number = 123457923
    rest1.email_address = "Joe@JoesPizza.co.uk"
    rest1.rating=4
    rest1.price=2
	rest1.picture = "/media/images/yum_9Gh9MpK.jpg"
    rest1.save()
    
    name = "Burger Place"
    rest2 = Restaurant.objects.get_or_create(owner=userP1,name="Burger Place",slug=slugify(name))[0]
    rest2.address = "10 Mitchell Lane"
    rest2.overview = "Char grilled burgers"
    rest2.detailed = "We serve any type of burger you can imagine!"
    rest2.phone_number = 21341234
    rest2.email_address = "Joe@BurgerPlace.co.uk"
    rest2.rating=4
    rest2.price=1
	rest1.picture = "/media/images/nom_ZkUoSM8.jpg"
    rest2.save()
    
    comment1 = Comment.objects.get_or_create(user=userP2,restaurant=rest1,rating=5,price=3,date_time=None)[0]
    comment1.comment = "Fantastic pizza restaurant, the 4 cheeses pizza was delicious"
    comment1.date_time=datetime.now()
    comment1.save()
    
    comment2 = Comment.objects.get_or_create(user=userP3,restaurant=rest1,rating=3,price=1,date_time=None)[0]
    comment2.comment = "Ok restaurant, too cheesy for me"
    comment2.date_time=datetime.now()
    comment2.save()
    
    comment3 = Comment.objects.get_or_create(user=userP2,restaurant=rest2,rating=4,price=1,date_time=None)[0]
    comment3.comment = "Delicious burgers and soda"
    comment3.date_time=datetime.now()
    comment3.save()
# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()