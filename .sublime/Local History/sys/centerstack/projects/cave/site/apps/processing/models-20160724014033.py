#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	members/models.py
#*=========================== #
from django.db import models
from tinymce.models import HTMLField
from members.models import Member
from django_xworkflows import models as wf
import datetime


# ==================================================#
#	Workflows
# ==================================================#
class Workflow(wf.Workflow):
	states = (
		('out', 'Checked Out'),
		('in', 'Checked In'),
	)
	transitions = (
		('check_in', 'out', 'in'),
		('check_out', 'in', 'out'),
	)
	initial_state = 'out'



class Processing(models.Model):
	member = models.ForeignKey(Member, null=True, blank=True)
	status = wf.StateField(Workflow, null=True, blank=True)

	def __unicode__(self):
		return str(self.member)












