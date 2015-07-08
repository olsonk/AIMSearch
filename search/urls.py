from django.conf.urls import patterns, url
from search import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	url(r'^grade/(?P<grade>\w+)/$', views.grade, name='grade'),
	url(r'^standard/(?P<pk>\d+)/$', views.StandardDetail.as_view(), name='standard'),
	url(r'^issues/(?P<issue>\d+)/$', views.issue, name='issue'),
)