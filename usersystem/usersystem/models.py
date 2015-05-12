
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
	PROGRAM_TAG = 'program'
	MATH_TAG = 'math'
	ABROAD_TAG = 'abroad'
	TAG_CHOICES = (
		(PROGRAM_TAG, '编程'),
		(MATH_TAG, '数学'),
		(ABROAD_TAG, '出国'),
	)
	user = models.ForeignKey(User, blank=True)
	title = models.TextField()
	description = models.TextField()
	tag = models.CharField(max_length=10, choices=TAG_CHOICES, blank=True)


class QuestionUrl(models.Model):
	CSDN = 'csdn'
	WEBSITE_CHOICE = (
		(CSDN, 'CSDN'),
	)
	question = models.ForeignKey(Question)
	website = models.CharField(max_length=5, choices=WEBSITE_CHOICE)
	url = models.URLField()


class Search(models.Model):
	title = models.TextField(default="")
	user = models.ForeignKey(User)


class Answer(models.Model):
	link = models.URLField()
	good = models.IntegerField()


class UserModel(models.Model):
	user = models.OneToOneField(User)
	imei = models.TextField(default="")
	voteAnswers = models.ManyToManyField(Answer)


