from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Group(models.Model):
	"""Group Model"""
	
	class Meta(object):
		verbose_name = u'Group'
		verbose_name_plural = u'Groups'
		
	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Title')
		
	leader = models.OneToOneField('Student',
		verbose_name=u'Leader',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)
	
	notes = models.TextField(
		blank=True,
		verbose_name=u'Additional notes')
		
	def __unicode__(self):
		if self.leader:
			return u'%s (%s %s)' %(self.title, self.leader.first_name, self.leader.last_name)
		else:
			return u'%s' %(self.title,)