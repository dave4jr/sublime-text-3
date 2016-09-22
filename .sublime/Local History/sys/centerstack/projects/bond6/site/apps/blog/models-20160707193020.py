#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	blog/models.py
#*========================== #
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime


class Group(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __unicode__(self):
		return self.name


class Blog(models.Model):
	title = models.CharField(max_length=50, blank=True, null=True)
	author = models.ForeignKey(User, blank=True, null=True)
	group = models.ForeignKey(Group, blank=True, null=True)
	datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def get_date(self):
		return self.datetime.date

	def get_time(self):
		return self.datetime.time

	date = property(get_date)
	time = property(get_time)

	img = models.ImageField(verbose_name="Image (1600 x 1000)", upload_to="blog/", blank=True, null=True)
	img_single = models.ImageField(verbose_name="Image (1600 x 571)", upload_to="blog/", blank=True, null=True)
	
	post =HTMLField(verbose_name="Post (Summary)", blank=True, null=True)
	post_single =HTMLField(verbose_name="Post (Single)", blank=True, null=True)

	class Meta:
	       verbose_name_plural = "Blog"

	def __unicode__(self):
		return self.title









