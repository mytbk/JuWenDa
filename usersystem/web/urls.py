from django.conf.urls import patterns, include, url

from web import views


urlpatterns = patterns(
	'',
    url(r'^index$', views.index, name='index'),
	url(r'^search$', views.search, name='search'),
	url(r'^answerlist$', views.answerlist, name='answerlist'),
	url(r'^createUser$', views.create_user, name='createUser'),
	url(r'^authenticateUser$', views.authenticate_user, name='authenticateUser'),
	url(r'^setPassword$', views.set_password, name='setPassword'),
	url(r'^askQuestion$', views.ask_question, name='askQuestion'),
	url(r'^searchAnswer$', views.search_answer, name='searchAnswer'),
	url(r'^getDetail/(?P<link>.*)$', views.get_detail, name='getDetail'),
	url(r'^upVote$', views.up_vote, name='upVote'),
	url(r'^getVote$', views.get_vote, name='getVote'),
)
