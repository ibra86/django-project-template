# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#Views for Students
def students_list(request):
	students = (
		{'id':1,
		 'first_name': u'Yana',
		 'last_name': u'Ibrahimova',
		 'ticket': 235,
		 'image': 'img/yana_ibrahimova.jpg'},
		{'id':2,
		 'first_name': u'Iryna',
		 'last_name': u'Davydenko',
		 'ticket': 2123,
		 'image': 'img/iryna_davydenko.jpg'},
		{'id':3,
		 'first_name': u'Masha',
		 'last_name': u'Lytvyniuk',
		 'ticket': 1639,
		 'image': 'img/masha_lytvyniuk.jpg'},
	)
	# print {request.scheme}, {request.get_host()}
	return render(request, 'students/students_list.html',{'students':students})
	
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
	
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' %sid)

#Views for Groups
def groups_list(request):
	groups = (
		{'id':1,
		 'name': u'MtM-21',
		 'leader': u'Yana Ibrahimova'},
		{'id':2,
		 'name': u'MtM-22',
		 'leader': u'Alisa Bila'},
		{'id':3,
		 'name': u'MtM-23',
		 'leader': u'Alina Bukhanska'},
	)
	return render(request, 'students/groups_list.html',{'groups':groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' %gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' %gid)	
	
