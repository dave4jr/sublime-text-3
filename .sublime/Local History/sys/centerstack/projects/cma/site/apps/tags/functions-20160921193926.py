#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	functions.py
#*========================== #
from datetime import datetime, date
from pprint import pprint as pp
import pickle
import calendar
import os, sys



#	Directory Size
# ====================================== #
def dirsize(path, include_hidden=False):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			if include_hidden:
				fp = os.path.join(dirpath, f)
				total_size += os.path.getsize(fp)
			else:
				if not f.startswith("."):
					fp = os.path.join(dirpath, f)
					total_size += os.path.getsize(fp)
	return total_size


#	Directory Contents
# ====================================== #
def dircontents(path, include_hidden=False):
	n = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			if include_hidden:
				n+=1
			else:
				if not f.startswith("."):
					n+=1
	return n


#	Looping Deep Nested JSON
# ====================================== #
def get_json(node, key):
	from itertools import chain
	try:
		if 'children' in node:
			if key is None:
				return [node] + list(chain.from_iterable([get_json(child, key) for child in node['children']]))
			else:
				return [node[key]] + list(chain.from_iterable([get_json(child, key) for child in node['children']]))
		else:
			if key is None:
				return [node]
			else:
				return [node[key]]
	except:
		return None




#	List Files
# ====================================== #
def listfiles(path):
	from easydict import EasyDict

	files = EasyDict()
	array_root = []
	array_short = []
	array_long = []
	array_types = []

	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			filename_long = os.path.join(root, filename)
			if not filename.startswith("."):
				array_short.append(filename)
				array_long.append(filename_long)
				array_root.append(root)

				if os.path.isfile(filename_long):
					array_types.append("file")
				elif os.path.isdir(filename_long):
					array_types.append("folder")
				else:
					array_types.append("other")

	files.short = array_short
	files.long = array_long
	files.root = array_root
	files.type = array_types

	return files






	for file in os.listdir(path):
		dirfile = os.path.join(path, file)
		if not file.startswith("."):
			files.append(file)
			dirfiles.append(dirfile)
			if os.path.isfile(dirfile):
				filetypes.append("file")
			elif os.path.isdir(dirfile):
				filetypes.append("folder")
			else:
				filetypes.append("other")


# base_path = os.path.join(settings.MEDIA_ROOT, "files")



#	Split
# ====================================== #
def splitpath(path):
	sections = []
	while 1:
		parts = os.path.split(path)
		if parts[0] == path:  # sentinel for absolute paths
			sections.insert(0, parts[0])
			break
		elif parts[1] == path: # sentinel for relative paths
			sections.insert(0, parts[1])
			break
		else:
			path = parts[0]
			sections.insert(0, parts[1])
	return sections





def monthdiff(start_period, end_period, decimal_places = 2):
	if start_period > end_period:
		raise Exception('Start is after end')
	if start_period.year == end_period.year and start_period.month == end_period.month:
		days_in_month = calendar.monthrange(start_period.year, start_period.month)[1]
		days_to_charge = end_period.day - start_period.day+1
		diff = round(float(days_to_charge)/float(days_in_month), decimal_places)
		return diff
	months = 0
	if start_period.day > 1:
		last_day_in_start_month = calendar.monthrange(start_period.year, start_period.month)[1]
		days_to_charge = last_day_in_start_month - start_period.day	+1
		months = months + round(float(days_to_charge)/float(last_day_in_start_month), decimal_places)
		start_period = datetime(start_period.year, start_period.month+1, 1)
	last_day_in_last_month = calendar.monthrange(end_period.year, end_period.month)[1]
	if end_period.day != last_day_in_last_month:
		months = months + round(float(end_period.day) / float(last_day_in_last_month), decimal_places)
		last_day_in_previous_month = calendar.monthrange(end_period.year, end_period.month - 1)[1]
		end_period = datetime(end_period.year, end_period.month - 1, last_day_in_previous_month)
	if start_period != end_period:
		months = months + (end_period.year - start_period.year) * 12 + (end_period.month - start_period.month) + 1
	diff = round(months, decimal_places)
	return diff




#	Dictobj
# ====================================== #
import pickle

class DictionaryObject(object):
	"""
	Copyright 2012 "Grim Apps"

	 Licensed under the Apache License, Version 2.0 (the "License");
	 you may not use this file except in compliance with the License.
	 You may obtain a copy of the License at

			 http://www.apache.org/licenses/LICENSE-2.0

	 Unless required by applicable law or agreed to in writing, software
	 distributed under the License is distributed on an "AS IS" BASIS,
	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 See the License for the specific language governing permissions and
	 limitations under the License.

	Helper class written by William Grim - grimwm
	Original repo: https://github.com/grimwm/py-dictobj
	Thank you!
	************************
	A class that has all the functionality of a normal Python dictionary, except
	for the fact it is itself immutable.  It also has the added feature of
	being able to lookup values by using keys as attributes.

	The reason for the class being immutable by default is to help make it a
	little easier to use in multiprocessing situations.  Granted, the underlying
	values themselves are not deeply copied, but the aim is to enforce some
	ensurances of immutability on the container class.

	When using positional arguments, the first argument must always be something
	that would be a valid argument for a dict().  However, a second, optional
	argument may be passed to create a default value when keys are not found.
	
	Examples:
		>>> d = DictionaryObject({'a':1, 'b':True, 3:'x'})
		>>> print d.a, d.b, d[3]
		1 True x
		
		>>> d = DictionaryObject((('a',1),('b',2)))
		>>> print d.a, d.b
		1 2
		
		>>> d = DictionaryObject(a=1, b=True)
		>>> print d
		DictionaryObject({'a': 1, 'b': True})

		>>> d = DictionaryObject({'a':1, 'b':True}, None)
		>>> print d.a, d.b, d.c, d.d
		1 True None None
		
		>>> d = DictionaryObject({'a':1}, None)
		>>> m = MutableDictionaryObject(d)
		>>> print d == m
		True
		>>> m.a = 0
		>>> print d == m, d < m, d > m, d != m, d <= m, d >= m
		False False True True False True
	
		>>> import pickle
		>>> m1 = MutableDictionaryObject({'a':1}, None)
		>>> m2 = pickle.loads(pickle.dumps(m1))
		>>> print m1 == m2
		True
		>>> m1.a = 3
		>>> print m1 == m2
		False
		>>> m1.a == 3
		True
		>>> m1['c'] = 5
		>>> m1['c']
		5
		"""
	def __init__(self, contents=(), *args, **kwargs):
		"""
		Take as input a dictionary-like object and return a DictionaryObject.
		It also makes sure any keys containing dictionaries are also converted
		to DictionaryObjects.
		"""
		super(DictionaryObject, self).__init__()
		if isinstance(contents, DictionaryObject):
			self.__dict__.update(pickle.loads(pickle.dumps(contents.__dict__)))
			return

		self.__dict__['_items'] = dict(contents, **kwargs)

		if len(args) > 1:
			raise TypeError("too many arguments")

		# If we have more than one argument passed in, use the second argument
		# as a default value.
		if args:
			try:
				default = type(self)(args[0])
			except:
				default = args[0]
			self.__dict__['_defaultValue'] = default
		else:
			self.__dict__['_defaultValue'] = None
		self.__dict__['_defaultIsSet'] = len(args) > 0

		for k in self._items:
			if isinstance(self._items[k], dict):
				self._items[k] = type(self)(self._items[k])

	def __setstate__(self, dict):
		self.__dict__.update(dict)

	def __getstate__(self):
		return self.__dict__.copy()

	def __getattr__(self, name):
		"""
		This is the method that makes all the magic happen.  Search for
		'name' in self._items and return the value if found.  If a default
		value has been set and 'name' is not found in self._items, return it.
		Otherwise raise an AttributeError.

		Example:
			>>> d = DictionaryObject({'keys':[1,2], 'values':3, 'x':1})
			>>> d.keys
			<bound method DictionaryObject.keys of DictionaryObject({'keys': [1, 2], 'x': 1, 'values': 3})>
			>>> d.values
			<bound method DictionaryObject.values of DictionaryObject({'keys': [1, 2], 'x': 1, 'values': 3})>
			>>> d.x
			1
			>>> d['keys']
			[1, 2]
			>>> d['values']
			3
		"""
		if name in self._items:
			return self._items[name]
		if self._defaultIsSet:
			return self._defaultValue
		raise AttributeError("'%s' object has no attribute '%s'" % (type(self).__name__, name))

	def __setattr__(self, name, value):
		"""
		This class is immutable-by-default.  See MutableDictionaryObject.
		"""
		raise AttributeError("'%s' object does not support assignment" % type(self).__name__)

	def __getitem__(self, name):
		return self._items[name]
		
	def __contains__(self, name):
		return name in self._items
		
	def __len__(self):
		return len(self._items)
		
	def __iter__(self):
		return iter(self._items)
			
	def __repr__(self):
		if self._defaultIsSet:
			params = "%s, %s" % (repr(self._items), self._defaultValue)
		else:
			params = repr(self._items)
		return "%s(%s)" % (type(self).__name__, params)
		
	def __cmp__(self, rhs):
		if self < rhs:
			return -1
		if self > rhs:
			return 1
		return 0

	def __eq__(self, rhs):
		val = cmp(self._items, rhs._items)
		if 0 == val:
			return 0 == cmp(self._defaultValue, rhs._defaultValue)
		return 0 == val

	def __ne__(self, rhs):
		return not (self == rhs)

	def __lt__(self, rhs):
		val = cmp(self._items, rhs._items)
		if 0 == val:
			return -1 == cmp(self._defaultValue, rhs._defaultValue)
		return -1 == val

	def __le__(self, rhs):
		return self < rhs or self == rhs

	def __gt__(self, rhs):
		return not (self <= rhs)

	def __ge__(self, rhs):
		return self > rhs or self == rhs

	def keys(self):
		return self._items.keys()
		
	def values(self):
		return self._items.values()

	def asdict(self):
		"""
		Copy the data back out of here and into a dict.  Then return it.
		Some libraries may check specifically for dict objects, such
		as the json library; so, this makes it convenient to get the data
		back out.

		>>> import dictobj
		>>> d = {'a':1, 'b':2}
		>>> dictobj.DictionaryObject(d).asdict() == d
		True
		>>> d['c'] = {1:2, 3:4}
		>>> dictobj.DictionaryObject(d).asdict() == d
		True
		"""
		items = {}
		for name in self._items:
			value = self._items[name]
			if isinstance(value, DictionaryObject):
				items[name] = value.asdict()
			else:
				items[name] = value
		return items

class MutableDictionaryObject(DictionaryObject):
	"""
	Slight enhancement of the DictionaryObject allowing one to add
	attributes easily, in cases where that functionality is wanted.

	Examples:
		>>> d = MutableDictionaryObject({'a':1, 'b':True}, None)
		>>> print d.a, d.b, d.c, d.d
		1 True None None
		>>> d.c = 3
		>>> del d.a
		>>> print d.a, d.b, d.c, d.d
		None True 3 None
	"""
	def __setattr__(self, name, value):
		self._items[name] = value

	def __delattr__(self, name):
		del self._items[name]
		
	__setitem__ = __setattr__
	__delitem__ = __delattr__






