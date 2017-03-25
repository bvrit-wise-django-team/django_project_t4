from django.conf.urls import url

from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
	url(r'^tpo/dashboard/$', tpo_dashboard, name='tpo_dashboard'),
]