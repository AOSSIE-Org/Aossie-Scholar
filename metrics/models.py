from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class ScholarProfile(models.Model):
	author_name= models.CharField(max_length=100)
	profile_url= models.URLField(max_length=200, primary_key= True)
	publication_title= ArrayField(models.CharField(max_length=500))
	normalized_citations= ArrayField(models.CharField(max_length=50), null= True)
	created_at= models.DateTimeField(auto_now_add= True)
	def __str__(self):
		return (self.author_name)
