from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class ScholarProfile(models.Model):
	author_name= models.CharField(max_length=100)
	profile_url= models.URLField(max_length=200, primary_key= True)
	publication_title= ArrayField(models.CharField(max_length=500))
	normalized_citations= ArrayField(models.CharField(max_length=50), null= True)
	citations= ArrayField(models.CharField(max_length=50), null= True)
	coAuthors= ArrayField(models.CharField(max_length=50), null= True)
	created_at= models.DateTimeField(auto_now_add= True)
	country= models.CharField(max_length=100, null= True)
	publications= models.CharField(max_length=100, null= True)
	Tcitations= models.CharField(max_length=100, null= True)
	Hindex= models.CharField(max_length=100, null= True)
	Gindex= models.CharField(max_length=100, null= True)
	Mindex= models.CharField(max_length=100, null= True)
	Year= ArrayField(models.CharField(max_length=100), null=True)
	
	def __str__(self):
		return (self.author_name)
