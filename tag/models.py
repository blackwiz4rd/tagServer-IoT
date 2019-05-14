from django.db import models
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User

class Validate(models.Model):
	tag = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	date = models.DateTimeField()
	
