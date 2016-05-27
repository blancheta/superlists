from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class User(models.Model):
	email = models.EmailField(primary_key=True)
	last_login = models.DateTimeField(default=timezone.now)
	REQUIRED_FIELDS = ()
	USERNAME_FIELD = 'email'

	def set_password(self,password):
		pass

	def is_authenticated(self):
		return True

	objects = BaseUserManager()
