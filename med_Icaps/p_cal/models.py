import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Shift(models.Model):
	shift_time_start = models.DateTimeField('Shift Start Time')
	shift_time_end = models.DateTimeField('Shift End Time')	
	shift_location = models.CharField(max_length=200)
	physician = models.CharField(max_length=200)


	def __str__(self):
		return self.shift_location
	

class Physician(models.Model):
	name_first = models.CharField(max_length=200)
	name_last = models.CharField(max_length=200)
	specialty = models.CharField(max_length=200)

	def __str__(self):
		return self.name_first + " " + self.name_last

