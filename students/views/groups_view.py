# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from ..models.group_model import Group


#Views for Groups
def groups_list(request):
	groups = Group.objects.all()
	return render(request, 'students/groups_list.html',{'groups':groups})

# def groups_list(request):
	# groups = (
		# {'id':1,
		 # 'name': u'MtM-21',
		 # 'leader': u'Yana Ibrahimova'},
		# {'id':2,
		 # 'name': u'MtM-22',
		 # 'leader': u'Alisa Bila'},
		# {'id':3,
		 # 'name': u'MtM-23',
		 # 'leader': u'Alina Bukhanska'},
	# )
	# return render(request, 'students/groups_list.html',{'groups':groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' %gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' %gid)	
	
