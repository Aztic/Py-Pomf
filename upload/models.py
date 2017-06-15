from django.db import models


class Upload(models.Model):
	user_id = models.IntegerField(default=0)
	filename = models.CharField(max_length=128)
	hash_value = models.CharField(max_length=128)
	original_filename = models.CharField(max_length=128)
	size = models.IntegerField(default=0)
	created = models.DateTimeField()

class User(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=128)
	token = models.CharField(max_length=128)
	email = models.CharField(max_length=64)

	def __str__(self):
		return self.name