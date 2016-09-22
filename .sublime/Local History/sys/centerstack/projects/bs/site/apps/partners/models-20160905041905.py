#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/models.py
#*=========================== #
from django.db import models
from tinymce.models import HTMLField
import datetime


class Partner(models.Model):
	img_banner = models.ImageField(upload_to="", blank=True, null=True)
	name = models.CharField(max_length=100, blank=True, null=True)
	text_intro = HTMLField(blank=True, null=True)
	
	img_collage_big = models.ImageField(upload_to="", blank=True, null=True)
	img_banner_medium = models.ImageField(upload_to="", blank=True, null=True)
	img_banner_small_1 = models.ImageField(upload_to="", blank=True, null=True)
	img_banner_small_2 = models.ImageField(upload_to="", blank=True, null=True)
	
	need_floor_plans_section = models.BooleanField(default=1)
	text_floor_plans = HTMLField(blank=True, null=True)
	img_floor_plans_1 = models.ImageField(upload_to="", blank=True, null=True)
	img_floor_plans_2 = models.ImageField(upload_to="", blank=True, null=True)
	img_floor_plans_3 = models.ImageField(upload_to="", blank=True, null=True)
	class Meta:
	       verbose_name_plural = "Partners"

	def __unicode__(self):
		return self.name









