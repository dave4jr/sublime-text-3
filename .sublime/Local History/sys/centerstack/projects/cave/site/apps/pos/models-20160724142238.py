#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments.py
#*========================== #
from django.db import models
from django.conf import settings
from members.models import Member
from inventory.models import Inventory



class ItemType(models.Model):
	name = models.CharField(max_length=300, blank=True, null=True)

	class Meta:
		verbose_name = "Item Type"
		
	def __unicode__(self):
		return self.name




class POS(models.Model):
	member = models.ForeignKey(Member, null=True, blank=True)
	item_type = models.ForeignKey(ItemType, null=True, blank=True)

	class Meta:
        	verbose_name_plural = "Point-Of-Sale"

	def __unicode__(self):
		return str(self.member)

 













