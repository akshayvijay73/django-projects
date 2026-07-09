from django.db import models
from django.contrib.auth.models import User

# Create student models (linked to Django 'User').
# OneToOne with 'User'

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	department = models.CharField(max_length=100)
	year  = models.IntegerField()

	def __str__(self):
		return self.User.username

