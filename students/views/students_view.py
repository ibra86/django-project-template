# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

from django.forms import ModelForm
from django.views.generic import UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models.student_model import Student
from ..models.group_model import Group

from ..util import paginate, get_current_group


class StudentUpdateForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__' # amendment comparing to book
	
	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)
	
		# set form tag attributes
		self.helper.form_action = reverse('students_edit', kwargs={'pk':kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		
		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
		# add buttons
		self.helper.layout.append(FormActions( # ammendment - dueto bug in the book
			Submit('add_button', 'Save', css_class='btn btn-primary'),
			Submit('cancel_button', 'Cancel', css_class='btn btn-link'),
			))
		

class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm
	
	def get_success_url(self):
		return u'%s?status_message=Student added successfully!' %(reverse('home'))
		
	def post(self, request, *args, **kwargs):
		# import pdb; pdb.set_trace()
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u"%s?status_message=Student's editing cancelled!" %(reverse('home')))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)
		
		# HttpResponseRedirect(u'%s?status_message=%s' %(reverse('contact_admin'), message))

	
class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'
	
	def get_success_url(self):
		return '%s?status_message=Deleted student successfully!'%reverse('home')


#Views for Students
def students_list(request):

	# check if we need to show only one group of students
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group=current_group)
	else:
		# otherwise show all students
		students = Student.objects.all()
	
	#try to order students list
	order_by = request.GET.get('order_by','')
	if order_by in ('last_name','first_name','ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse','')=='1':
			students = students.reverse()
	# elif order_by == '':
		# students = students.order_by('last_name')
		
	#apply pagination, 3 students per page
	context = paginate(students, 3, request, {}, var_name='students')
	
	return render(request,'students/students_list.html',context)
	
	# # OLD PAGINATOR
	# paginator = Paginator(students,3)
	# page = request.GET.get('page')
	# try:
		# students = paginator.page(page)
	# except PageNotAnInteger:
		# # If page is not an integer, deliver first page
		# students = paginator.page(1)
	# except EmptyPage:
		# # If page is out of range (e.g. 9999), deliver last page of results
		# students = paginator.page(paginator.num_pages)
	# return render(request, 'students/students_list.html', {'students':students})

	
def students_add(request):
	#was form posted?
	if request.method == 'POST':
	
		#was form add button clicked?
		if request.POST.get('add_button') is not None:			
			#error collection
			errors = {}
			#validated student data will go here
			data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}
			
			#validate user input
			first_name = request.POST.get('first_name','').strip()
			if not first_name:
				errors['first_name'] = u'Name is obligatory'
			else:
				data['first_name'] = first_name
				
			last_name = request.POST.get('last_name','').strip()
			if not last_name:
				errors['last_name'] = u'Surname is obligatory'
			else:
				data['last_name'] = last_name
				
			birthday = request.POST.get('birthday','').strip()
			if not birthday:
				errors['birthday'] = u'Birthday is obligatory'
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u'Enter correct date format (e.g. 1984-12-30)'
				else:
					data['birthday'] = birthday
				
			ticket = request.POST.get('ticket','').strip()
			if not ticket:
				errors['ticket'] = u'Ticket number is obligatory'
			else:
				data['ticket'] = ticket
			
			student_group = request.POST.get('student_group','').strip()
			if not student_group:
				errors['student_group'] = u"Choose student's group"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u'Choose correct group'
				else:
					data['student_group'] = groups[0]
				
			photo = request.FILES.get('photo')
			if photo:
				data['photo'] = photo
				
				
			#save student
			if not errors:
				student = Student(**data)
				student.save()
				
				#redirect user to students list
				return HttpResponseRedirect(u'%s?status_message=Student %s %s added successfully!' %(reverse('home'),first_name,last_name))
			
			else:
				#render form with errors and previous user input
				return render(request, 'students/students_add.html',{'groups':Group.objects.all().order_by('title'),'errors':errors})
		
		elif request.POST.get('cancel_button') is not None:
			#redirect to home page on cancel button
			return HttpResponseRedirect(u'%s?status_message=Adding student cancelled!' %reverse('home'))
	
	else:
		#initial form render
		return render(request, 'students/students_add.html',{'groups':Group.objects.all().order_by('title')})
	
# def students_edit(request, sid):
	# return HttpResponse('<h1>Edit Student %s</h1>' %sid)

# def students_delete(request, sid):
	# return HttpResponse('<h1>Delete Student %s</h1>' %sid)