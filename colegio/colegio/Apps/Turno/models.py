from django.db import models

class Turno(models.Model):
	Nombre = models.CharField(max_length=60)
	
	def __str__(self):
		return self.Nombre	