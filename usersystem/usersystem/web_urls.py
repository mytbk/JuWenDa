from django.conf.urls import patterns, include, url
from django.contrib import admin
from usersystem import web_views

urlpatterns = patterns(
	'',
	url(r'^createUser$', web_views.create_user, name='createUser'),
	url(r'^authenticateUser$', web_views.authenticate_user, name='authenticateUser'),
	url(r'^setPassword$', web_views.set_password, name='setPassword'),
	url(r'^askQuestion$', web_views.ask_question, name='askQuestion'),
	url(r'^searchAnswer$', web_views.search_answer, name='searchAnswer'),
	url(r'^getDetail$', web_views.get_detail, name='getDetail$'),
	url(r'^upVote$', web_views.up_vote, name='upVote$'),
	url(r'^getVote$', web_views.get_vote, name='getVote$'),
	url(r'^admin/', include(admin.site.urls)),
)
