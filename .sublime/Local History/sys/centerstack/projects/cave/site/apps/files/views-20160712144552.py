# -*- coding: utf-8 -*-
#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	files/views.py
#*======================== #
import os, os.path, sys, json, logging, shutil, time, datetime
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import DocumentForm
from .models import Document
from tags.functions import dirsize
from tags.functions import dircontents
from django.conf import settings
import jstree



#	TreeView
# ====================================== #
def main(request, template):
	paths = []
	id_mapping = {}
	k = 1
	base = os.path.join(settings.MEDIA_ROOT)
	for root, dirs, files in os.walk(base):

		#	Files
		# ====================================== #
		for name in files:
			if not name.startswith("."):
				path_long = os.path.join(root, name)
				path = path_long[len(base)+1:len(path_long)]

				#	File Type Mapping
				# ====================================== #
				fn, ext = os.path.splitext(name)
				ext = ext[1:].upper()
				if ext in ["XLR", "XLS", "XLSX"]:
					icon_type = "file_xls"
				elif ext in ["PPT", "PPS", "PPTX"]:
					icon_type = "file_ppt"
				elif ext in ["DOC", "DOCX"]:
					icon_type = "file_doc"
				elif ext in ["ZIP", "TAR", "GZIP,"]:
					icon_type = "file_archive"
				elif ext in ["HTML", "XML", "XHTML", "CSS", "SCSS", "JS", "PY"]:
					icon_type = "file_code"
				elif ext in ["PDF"]:
					icon_type = "file_pdf"
				elif ext in ["ASF", "AVI", "FLV", "M4V", "MOV", "MP4", "MPG", "RM", "SRT", "SWF", "VOB", "WMV"]:
					icon_type = "file_video"
				elif ext in ["AIF", "M3U", "M4A", "MID", "MP3", "MPA", "WAV", "WMA"]:
					icon_type = "file_audio"
				elif ext in ["BMP", "DDS", "GIF", "JPG", "PNG", "PSD", "PSP", "TGA", "THM", "TIF", "TIF", "YUV", "ect", "AI", "EPS", "PS", "SVG"]:
					icon_type = "file_image"
				else:
					icon_type = "file"


				#	Input File Metadata
				# ====================================== #
				filetype = icon_type[5:].capitalize()
				(mode, ino, dev, nlink, uid, gid, filesize, atime, mtime, ctime) = os.stat(path_long)
				filesize = "%s KB" % (filesize / 1000)

				modified_floating = os.path.getmtime(path_long)
				created_floating = os.path.getctime(path_long)

				modified = str(datetime.datetime.fromtimestamp(modified_floating))
				created = str(datetime.datetime.fromtimestamp(created_floating))

				tree = jstree.Path(path, k, {"type":icon_type, "data": {"filesize":filesize, "filetype":filetype, "contents":"-", "sort_order":0 }})

				paths.append(tree)
				id_mapping[k] = path
				id_mapping["type"] = "file"
				k+=1


		#	Folders
		# ====================================== #
		for name in dirs:
			path_long = os.path.join(root, name)
			path = path_long[len(base)+1:len(path_long)]
			logging.debug(name)

			(mode, ino, dev, nlink, uid, gid, filesize, atime, mtime, ctime) = os.stat(path_long)
			filesize = dirsize(path_long)
			filesize = "%s KB" % (filesize / 1000)
			contents = dircontents(path_long)

			if name == "Check-Out":
				sort_order = 3
				icon_type = "folder_system"
			elif name == "Check-In":
				sort_order = 2
				icon_type = "folder_system"
			elif name == "Inventory":
				sort_order = 3
				icon_type = "folder_system"
			elif name == "Files":
				sort_order = 5
				icon_type = "folder_root"
				folder_root_id = k
			elif name == "Users":
				sort_order = 1
				icon_type = "folder_system"
				folder_root_id = k
			else:
				sort_order = 4
				icon_type = "folder"

			tree = jstree.Path(path, k, {"type":icon_type, "data": {"filesize":filesize, "filetype":"Directory", "contents": contents, "sort_order":sort_order }})

			paths.append(tree)
			id_mapping[k] = path
			id_mapping["type"] = "folder"
			k+=1
	t = jstree.JSTree(paths)
	node_json = t.jsonData()


	#	Delete Checked Files/Folders
	# ====================================== #
	if request.method == "POST":
		id_string = str(request.POST.getlist('tree-checkbox')).strip("[u']")
		id_array = id_string.split(",")
		for id in id_array:
			node = id_mapping[int(id)]
			
			if node == "Check-In" or node == "Check-Out" or node=="Files" or node=="Inventory" or node=="Users":
				messages.add_message(request, messages.ERROR, 'Checkin, Checkout, Files, Inventory, and Users folders are used to keep system files and can not be deleted.')
				return redirect('files')
			else:
				file = os.path.join(base, node)
				if os.path.isfile(file):
					os.remove(file)
				elif os.path.isdir(file):
					shutil.rmtree(file)
				else:
					messages.add_message(request, messages.ERROR, 'Unkown File Type.')

		return redirect('files')

	context = {
		"json": node_json,
		"folder_root_id": folder_root_id,
	}
	return render(request, template, context)



#	New Folder
# ====================================== #
def new_folder(request, template):
	base = os.path.join(settings.MEDIA_ROOT)
	response_data = {}
	if request.method == "POST":
		folder_name = str(request.POST.getlist('folder_name')).strip("[u']")
		path = os.path.join(base, folder_name)

		if os.path.isdir(path):
			response_data['alerts'] = "exists"
		else:
			os.makedirs(path)
			response_data['alerts'] = "created"

		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return HttpResponse("No Data!")







