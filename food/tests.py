from django.test import TestCase

from food.models import Restaurant
from food.models import Comment
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
