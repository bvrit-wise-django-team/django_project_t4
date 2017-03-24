from django.conf.urls import url
from student import views
from django.contrib import admin

urlpatterns=[url(r'^index/$',views.index,name='index'),
				url(r'^success/$',views.success,name='success'),
				url(r'^acadamicdetails/$',views.acadamicdetails,name='acadamicdetails'),
				url(r'^additionaldetails/$',views.additionaldetails,name='additionaldetails')]

