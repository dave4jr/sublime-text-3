#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 blog/urls.py
#*====================== #
from django.conf.urls import patterns, url, include
from django.contrib import admin
from . import views as blog_views
admin.autodiscover()


#	Blog
# ========================================= #
urlpatterns = [
	url(r'^$', blog_views.main, {"template":"blog.html"}, name="blog"),
	url(r'^(?P<pk>\w+)/$', blog_views.single, {"template":"blog-single.html"}, name="blog-single"),
]

	

