# -*- coding: utf-8 -*-
from django.db import models

class MonthJournal(models.Model):
	"""Student Monthly Journal"""
	
	# for admin page
	class Meta:
		verbose_name = 'Monthly Journal'
		verbose_name_plural = 'Monthly Journals'
		
	student = models.ForeignKey('Student',
		verbose_name = 'Student',
		blank = False,
		unique_for_month = 'date')
		
	# we only need year and moth, so always set day to first day of the month
	date = models.DateField(
		verbose_name = 'Date',
		blank = False)
		
	# list of days, each says whether student was present or not
	day = locals()
	for i in range(1,32):
		day['present_day'+str(i)]=models.BooleanField(default=False)
	
	def __unicode__(self):
		return '%s: %d, %d' %(self.student.last_name, self.date.month, self.date.year)