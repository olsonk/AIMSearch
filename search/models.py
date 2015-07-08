from django.db import models

# Create your models here.
class Standard(models.Model):
	code = models.CharField(max_length=15)
	text = models.TextField()
	
	def __unicode__(self):
		return self.code
	
class Issue(models.Model):
	AIMS = 'AIMS Magazine'
	CLASSROOM_MAILBOX = 'Classroom Mailbox'
	OTHER = 'Other'
	name_choices = (
					(AIMS, 'AIMS Magazine'),
					(CLASSROOM_MAILBOX, 'Classroom Mailbox'),
					(OTHER, 'Other'),
					)
	source_name = models.CharField(	max_length = 30,
								choices = name_choices,
								default = AIMS)
	
	vol = models.CharField(max_length=5)
	no = models.PositiveIntegerField()
	year = models.CharField(max_length=15)
	
	def __unicode__(self):
		return self.year
	
class Activity(models.Model):
	issue = models.ForeignKey(Issue)
	standards = models.ManyToManyField(Standard)
	title = models.CharField(max_length=100)
	description = models.TextField()
	goals = models.TextField()
	
	def __unicode__(self):
		return self.title