from django.conf.urls import patterns, include, url
from django.contrib import admin
from usersystem import phone_views
from usersystem import phone_urls

urlpatterns = patterns(
	'',
    url(r'^phone/', include(phone_urls, namespace='phone')),
    url(r'^web/', include(phone_urls, namespace='phone')),
	url(r'^admin/', include(admin.site.urls)),
)
