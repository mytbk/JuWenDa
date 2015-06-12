from django.conf.urls import patterns, include, url
from django.contrib import admin
from usersystem import phone_views

urlpatterns = patterns(
	'',
	url(r'^isCreated$', phone_views.is_created, name='isCreated'),
	url(r'^createUser$', phone_views.create_user, name='createUser'),
	url(r'^authenticateUser$', phone_views.authenticate_user, name='authenticateUser'),
	url(r'^setPassword$', phone_views.set_password, name='setPassword'),
	url(r'^setUsername$', phone_views.set_username, name='setUsername'),
	url(r'^askQuestion$', phone_views.ask_question, name='askQuestion'),
	url(r'^searchAnswer$', phone_views.search_answer, name='searchAnswer'),
	url(r'^getDetail$', phone_views.get_detail, name='getDetail$'),
	url(r'^upVote$', phone_views.up_vote, name='upVote$'),
	url(r'^getVote$', phone_views.get_vote, name='getVote$'),
	url(r'^admin/', include(admin.site.urls)),
)
