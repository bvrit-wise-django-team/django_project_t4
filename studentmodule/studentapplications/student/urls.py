from django.conf.urls import url
from student import views
from django.contrib import admin

urlpatterns=[url(r'^index/$',views.index,name='index'),
				url(r'^success/(?P<sid>\w+)/$',views.success,name='success'),
				url(r'^acadamicdetails/(?P<sid>\w+)/$',views.acadamicdetails,name='acadamicdetails'),
				url(r'^additionaldetails/(?P<sid>\w+)/$',views.additionaldetails,name='additionaldetails'),
				url(r'^editpersonal/(?P<sid>\w+)/$',views.editpersonal,name='editpersonal'),]

