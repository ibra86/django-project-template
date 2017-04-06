from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	"""Student Model"""
	
	class Meta(object):
		verbose_name = 'Student'
		verbose_name_plural = u'Students'
	
	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Name')
	
	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Surname')
		
	middle_name = models.CharField(
		max_length=256,
		blank=True,
		verbose_name=u'Patronimic',
		default='')
		
	birthday = models.DateField(
		blank=False,
		verbose_name=u'Birthday',
		null=True)
	
	photo = models.ImageField(
		blank=True,
		verbose_name=u'Photo',
		null=True)
	
	ticket = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Tickets')
	
	notes = models.TextField(
		blank=True,
		verbose_name=u'Additional notes')
		
	student_group = models.ForeignKey('Group',
		verbose_name=u'Group',
		blank=False,
		null=True,
		on_delete=models.PROTECT)
		
	def __unicode__(self):
		return u'%s %s' %(self.first_name, self.last_name)