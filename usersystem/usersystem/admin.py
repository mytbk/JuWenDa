
from django.contrib import admin
from usersystem.models import UserModel, Question, QuestionUrl, Search

admin.site.register(UserModel)
admin.site.register(Question)
admin.site.register(QuestionUrl)
admin.site.register(Search)