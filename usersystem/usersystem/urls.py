from django.conf.urls import patterns, include, url
from django.contrib import admin
from usersystem import phone_urls
import web

urlpatterns = patterns(
	'',
    url(r'^phone/', include(phone_urls, namespace='phone')),
    url(r'^web/', include('web.urls', namespace='phone')),
	url(r'^admin/', include(admin.site.urls)),
)
