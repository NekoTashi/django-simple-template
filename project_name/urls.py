# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	# Example:
	# url(r'^', include('{{ project_name }}.apps.<app_name>.urls')),
	url(r'^admin/', include(admin.site.urls)),
]