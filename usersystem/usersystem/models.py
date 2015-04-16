
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
	pass


class Answer(models.Model):
	pass


class UserModel(models.Model):
	user = models.OneToOneField(User)
	imei = models.TextField(default="")