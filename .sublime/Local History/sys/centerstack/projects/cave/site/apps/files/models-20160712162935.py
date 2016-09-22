#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	files/models.py
#*=========================== #
from __future__ import unicode_literals
from django.db import models
import os, sys, os.path
from django.contrib.auth.models import User
from django.conf import settings
from tags.functions import splitpath
from django.core.files.storage import FileSystemStorage
import logging


class OverwriteStorage(FileSystemStorage):
	def get_available_name(self, name):
		if self.exists(name):
			os.remove(os.path.join(settings.MEDIA_ROOT, name))
		return name


class Document(models.Model):
	file = models.FileField(max_length=50, upload_to="files", storage=OverwriteStorage(), blank=True)

	def spath(self):
		return splitpath(str(self.file))
	spath = property(spath)
	
	def levels(self):
		c = len(self.spath)-1
		if c == 0:
			return "root"
		else:
			return c
	levels = property(levels)


	def file_or_folder(self):
		for ii in self.spath:
			return ii
	file_or_folder = property(file_or_folder)


	def name(self):
		fn = str(self.file).lower()
		return os.path.basename(fn)
	name = property(name)
	
	def size_mb(self):
		return self.file.size / 1000
	size_mb = property(size_mb)

	user = models.ForeignKey(User, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)
	def __unicode__(self):
		return str(self.file.name)







