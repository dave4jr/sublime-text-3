#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	blog/models.py
#*========================== #
from django.db import models
import datetime
import logging

project_types = []

class Budget(models.Model):
	budget_range = models.CharField(max_length=30,  null=True, blank=True)
	sort_order = models.IntegerField(null=True, blank=True)
	def __unicode__(self):
		return self.budget_range


class Planner(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	company = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)

	#	Project Types
	# ====================================== #
	website = models.BooleanField(blank=True)
	application = models.BooleanField(blank=True)
	logo = models.BooleanField(blank=True)
	ecommerce = models.BooleanField(blank=True)
	seo = models.BooleanField(blank=True)
	other = models.BooleanField(blank=True)


	def get_project_type(self):
		project_types = []
		types = [ self.website, self.application, self.logo, self.ecommerce, self.seo, self.other ]
		type_names = ["Website / UI", "Web Application / System", "Logo / Branding", "E-Commerce", "SEO / Social Media", "Other"]
		for ii in range(len(types)):
			if types[ii]:
				project_types.append(type_names[ii])
		return ", ".join(project_types)


	project_types = property(get_project_type)
	description = models.TextField(null=True, blank=True)
	start = models.DateField(null=True, blank=True)
	end = models.DateField(null=True, blank=True)
	rush = models.BooleanField(verbose_name="No Rush", blank=True)
	budget = models.ForeignKey(Budget, null=True, default="$5,000 - $10,000")
	created = models.DateField(auto_now_add=True, null=True)

	class Meta:
	       verbose_name_plural = "Planner"

	def __unicode__(self):
		return self.name









