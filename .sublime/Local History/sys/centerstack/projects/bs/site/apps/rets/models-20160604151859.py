#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/upload_data.py
#*========================== #
from __future__ import unicode_literals
from django.db import models
from annoying.fields import JSONField
import datetime


class RetsData(models.Model):
	json = JSONField(blank=True, null=True)
	update = models.DateTimeField(auto_now=True, null=True, blank=True)

	def __unicode__(self):
		return str(self.json)




