from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # home page     
    url(r'^$', 'app_SpeakHub.views.home',name='home'), 
)


