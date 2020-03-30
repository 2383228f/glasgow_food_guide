from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, AutoField, IntegerField,\
	EmailField



# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	username = CharField(max_length=100, default="hello")
	is_owner = models.BooleanField(default=False)
	verified_by = models.ForeignKey('self',on_delete=models.CASCADE, related_name='+',blank = True, null = True)
	
	def __str__(self):
		return self.username
	
class Restaurant(models.Model):
	Restaurant_ID = AutoField(primary_key=True)
	owner = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null=True,blank=True)
	name = CharField(max_length = 100)
	address = CharField(max_length = 100, blank=True, null=True)
	overview = CharField(max_length = 100)
	detailed = CharField(max_length = 300, blank=True, null=True)
	phone_number = IntegerField(blank=True, null=True)
	email_address = EmailField(blank=True, null=True)
	rating = IntegerField(default=0)
	price = IntegerField(default=0)
	
	def __str__(self):
		return self.name
	