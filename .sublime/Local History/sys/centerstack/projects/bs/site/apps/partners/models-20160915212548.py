#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/models.py
#*=========================== #
from django.db import models
import datetime



class Group(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return self.name


class Partner(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	group = models.ForeignKey(Group, blank=True, null=True)
	website = models.CharField(max_length=100, blank=True, null=True)
	text_intro = models.TextField(verbose_name="Introduction", blank=True, null=True)
	text_summary = models.TextField(verbose_name="Summary", blank=True, null=True)
	
	img_banner = models.ImageField(upload_to="", verbose_name="Banner", blank=True, null=True)
	img_logo = models.ImageField(upload_to="", verbose_name="Logo", blank=True, null=True)
	img_collage_big = models.ImageField(upload_to="", verbose_name="Collage (Big)", blank=True, null=True)
	img_banner_medium = models.ImageField(upload_to="", verbose_name="Collage (Medium)", blank=True, null=True)
	img_banner_small_1 = models.ImageField(upload_to="", verbose_name="Collage (Small)", blank=True, null=True)
	img_banner_small_2 = models.ImageField(upload_to="", verbose_name="Collage (Small)", blank=True, null=True)
	
	need_floor_plans_section = models.BooleanField(default=1)
	text_floor_plans = models.TextField(blank=True, null=True)
	img_floor_plans_1 = models.ImageField(upload_to="", verbose_name="Floor Plan 1", blank=True, null=True)
	img_floor_plans_2 = models.ImageField(upload_to="", verbose_name="Floor Plan 2", blank=True, null=True)
	img_floor_plans_3 = models.ImageField(upload_to="", verbose_name="Floor Plan 3", blank=True, null=True)
	
	class Meta:
	       verbose_name_plural = "Partners"

	def __unicode__(self):
		return self.name









