from django.test import TestCase

from django.contrib.auth.models import User
from food.models import Restaurant
from food.models import Comment,UserProfile
class Tests(TestCase):
	#create restaurant
	def test_create_rest(self):
		rest = Restaurant(restaurant_ID = 14351)
		rest.save()
		self.assertEqual((rest.restaurant_ID), 14351)
	#restaurant default location is glasgow
	def test_create_rest(self):
		rest = Restaurant(restaurant_ID = 14351)
		rest.save()
		self.assertEqual(((rest.lat,rest.lng)), (55.8642,-4.2518))
	#create comment
	def test_create_rest(self):
		rest = Restaurant(restaurant_ID = 14214)
		rest.save()
		com = Comment(review_ID = 51453, rating =3, price =3,restaurant = rest)
		com.save()
		self.assertEqual((com.review_ID), 51453)
	#super user
	def test_create_super(self):
		user0 = User.objects.create_superuser(username="admin", email="admin@gfg.com",password="temp")
		user0.set_password("pass")
		user0.save()
		userP0 = UserProfile.objects.get_or_create(user=user0,username=user0.username,is_owner=True)[0]
		self.assertTrue(userP0)
