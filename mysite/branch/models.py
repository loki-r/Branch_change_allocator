from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Cat = (
	('GEN', 'GEN'),
	('OBC', 'OBC'),
	('SC', 'SC'),
	('ST', 'ST'),
	('PwD', 'PwD')
	)
class Info(models.Model):
	roll_no = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	present_branch = models.CharField(max_length=30)
	cpi = models.FloatField(max_length=30)
	category = models.CharField(choices=Cat,max_length=20)
	pref_1 = models.CharField(max_length=30)
	pref_2 = models.CharField(max_length=30)
	user = models.OneToOneField(User)
	def __unicode__(self):
		return self.name

class Document(models.Model):
    docfile = models.FileField(upload_to='csv_files')