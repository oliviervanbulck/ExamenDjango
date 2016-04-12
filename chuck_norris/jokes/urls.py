from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<first_name>[A-z ]+)/(?P<last_name>[A-z ]+)/$', views.joke, name='joke'),
]
