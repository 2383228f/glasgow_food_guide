from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, AutoField, IntegerField,EmailField
from django.template.defaultfilters import slugify
from django_mysql.models import ListCharField


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	username = CharField(max_length=100, default="hello")
	is_owner = models.BooleanField(default=False)
	verified_by = models.ForeignKey('self',on_delete=models.CASCADE, related_name='+',blank = True, null = True)
	favourites = ListCharField(max_length=100,base_field=CharField(max_length=100),null=True,blank=True,default='')
	def __str__(self):
		return self.username
	
class Restaurant(models.Model):
	restaurant_ID = AutoField(primary_key=True)
	owner = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null=True,blank=True)
	name = CharField(max_length = 100)
	slug = models.SlugField(unique=True)
	address = CharField(max_length = 100, blank=True, null=True)
	overview = CharField(max_length = 100)
	detailed = CharField(max_length = 300, blank=True, null=True)
	phone_number = IntegerField(blank=True, null=True)
	email_address = EmailField(blank=True, null=True)
	rating = IntegerField(default=0)
	price = IntegerField(default=0)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Restaurant, self).save(*args, **kwargs)
		
	def __str__(self):
		return self.name

class Comment(models.Model):
	review_ID = AutoField(primary_key=True)
	user = models.ForeignKey(UserProfile, on_delete = models.SET_NULL, null=True)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	date_time = models.DateTimeField(null=True)
	comment = CharField(max_length=1000)
	rating = IntegerField()
	price = IntegerField()
	
	def __str__(self):
		return self.user.username+", "+self.restaurant.name
	