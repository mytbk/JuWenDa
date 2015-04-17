
from django.contrib import admin
from usersystem.models import UserModel, Question, QuestionUrl

admin.site.register(UserModel)
admin.site.register(Question)
admin.site.register(QuestionUrl)