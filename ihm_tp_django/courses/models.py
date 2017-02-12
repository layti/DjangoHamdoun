from __future__ import unicode_literals

from django.db import models

class Professor(models.Model):
	name = models.CharField(max_length = 80)
	speciality = models.CharField(max_length = 80)
	birth_day = models.DateField(auto_now = False, auto_now_add = False)
	country = models.CharField(max_length = 80)

	def __str__(self):
		return self.name

class Module(models.Model):
	name = models.CharField(max_length = 80)
	department = models.CharField(max_length = 80)
	start_year = models.CharField(max_length = 4)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length = 80)
	module = models.ForeignKey('Module')
	professor = models.ForeignKey('Professor')
	nombre_heures = models.IntegerField()

	def __str__(self):
		return self.name
