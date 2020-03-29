from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	username = CharField(max_length=100, default="hello")
	is_owner = models.BooleanField(default=False)
	verified_by = models.ForeignKey('self',on_delete=models.CASCADE, related_name='+',blank = True, null = True)
	
	def __str__(self):
		return self.username