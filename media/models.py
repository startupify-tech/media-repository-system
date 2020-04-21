from django.db import models
from django.contrib.auth import get_user_model
#from .utility import get_file_path


User = get_user_model()


P = "PREMIUM"
F = "FREE"

TYPE_CHOICES = (
	(P, "Premium"),
	(F, "Free"),
)
NIL = "nil"

class topic(models.Model):
	Name = models.CharField(max_length=30, null=True)
	def __str__(self):
	  return self.Name

class media(models.Model):
	author	= models.ForeignKey(User,on_delete=models.CASCADE)
	title	= models.CharField(max_length=120)
	topics	= models.ForeignKey(topic, on_delete=models.CASCADE)
	event_date	= models.DateTimeField('Event date')
	discription	= models.TextField(blank=True,null=True)
	filename	= models.FileField(upload_to='uploads/')
	def __str__(self):
		return self.title

class subscriber(models.Model):
	Firstname   = models.CharField(max_length=30, null=True)
	Lastname    = models.CharField(max_length=30, null=True, blank=True)
	Email       = models.EmailField()
	Type        = models.CharField(max_length=30,choices=TYPE_CHOICES)
	Interest    = models.CharField(max_length=30, null=True)
	def __str__(self):
	  return self.Firstname

class vote(models.Model):
	Voted_by  = models.ForeignKey(subscriber, on_delete=models.SET_NULL, null=True, blank=True)
	Voted_for = models.ForeignKey(media, on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
	  return self.Voted_for

	