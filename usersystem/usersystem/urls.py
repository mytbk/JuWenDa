from django.conf.urls import patterns, include, url
from django.contrib import admin
from usersystem import views

urlpatterns = patterns(
	'',
	url(r'^isCreated$', views.is_created, name='isCreated'),
	url(r'^createUser$', views.create_user, name='createUser'),
	url(r'^authenticateUser$', views.authenticate_user, name='authenticateUser'),
	url(r'^setPassword$', views.set_password, name='setPassword'),
	url(r'^setUsername$', views.set_username, name='setUsername'),
	url(r'^askQuestion$', views.ask_question, name='askQuestion'),
	url(r'^searchAnswer$', views.search_answer, name='searchAnswer'),
	url(r'^getDetail$', views.get_detail, name='getDetail$'),
	url(r'^upVote$', views.up_vote, name='upVote$'),
	url(r'^getVote$', views.get_vote, name='getVote$'),
	url(r'^admin/', include(admin.site.urls)),
)
