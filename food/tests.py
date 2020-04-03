import os
import importlib
from django.conf import settings
from glasgow_food_guide.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE','glasgow_food_guide.settings')
from django.core.files import File

from django.urls import reverse
from django.test import TestCase

from django.contrib.auth.models import User
from food.models import Restaurant
from food.models import Comment,UserProfile
from django.template.defaultfilters import slugify
class Tests(TestCase):
	#create restaurant
	def test_create_rest(self):
		rest1 = Restaurant(restaurant_ID = 14214)
		rest1.save()
		self.assertTrue(rest1)
	#restaurant default location is glasgow
	def test_rest_default_location(self):
		rest = Restaurant(restaurant_ID = 14351)
		rest.save()
		self.assertEqual(((rest.lat,rest.lng)), (55.8642,-4.2518))
	#create comment
	def test_create_com(self):
		rest = Restaurant(restaurant_ID = 14214)
		rest.save()
		com = Comment(review_ID = 51453, rating =3, price =3,restaurant = rest)
		com.save()
		self.assertTrue(com)
	#create user
	def test_create_user(self):
		user1 = User.objects.get_or_create(username="JoePizza",email="joe@gmail.com",password="password")[0]
		userP1 = UserProfile.objects.get_or_create(user=user1,username=user1.username,is_owner=True)[0]
		user1.set_password("password")
		user1.save()
		self.assertTrue(user1)
	#create super user
	def test_create_superuser(self):
		user0 = User.objects.create_superuser(username="admin", email="admin@gfg.com",password="temp")
		user0.set_password("pass")
		user0.save()
		userP0 = UserProfile.objects.get_or_create(user=user0,username=user0.username,is_owner=True)[0]
		self.assertTrue(userP0)
	#upload picture
	def test_upload_picture(self):
		name = "Burger Place"
		user1 = User.objects.get_or_create(username="JoePizza",email="joe@gmail.com",password="password")[0]
		userP1 = UserProfile.objects.get_or_create(user=user1,username=user1.username,is_owner=True)[0]
		user1.save()
		rest1 = Restaurant.objects.get_or_create(owner=userP1,name="Joes Pizza",slug=slugify(name))[0]
		with open(os.path.join(BASE_DIR,'media/initial/pizza.jpg'),'rb') as f:
        		django_file = File(f)
        		rest1.picture.save('images/yum.jpg',django_file,save=True)
		rest1.save()
		with open(os.path.join(BASE_DIR,'media/initial/pizza.jpg'),'rb') as f:
			self.assertTrue(f)
	#test template dict exists
	def test_templates_directory_exists(self):
		project_base_dir = os.getcwd()
		templates_dir = os.path.join(project_base_dir, 'templates')
		directory_exists = os.path.isdir(templates_dir)
		self.assertTrue(directory_exists)


		
	
		


