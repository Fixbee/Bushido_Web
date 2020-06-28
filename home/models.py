from django.db import models


class Articles(models.Model):
	title = models.CharField(max_length = 30)
	slug = models.SlugField()
	description = models.TextField()
	images = models.ImageField(upload_to='images')
	date = models.DateTimeField('auto_now_add')

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'Articles'
		verbose_name = 'Bushido Articles'

class NewRegistration(models.Model):
	first_name = models.CharField(max_length=20)
	second_name = models.CharField(max_length=20)
	GENDER_CHOICE = (
		("M", "Male"),
		("F", "Female"),
		("Others", "Others")

		)
	gender = models.CharField(max_length=6, choices = GENDER_CHOICE, default='gender')
	phone_number = models.CharField(max_length=12)
	address = models.TextField(null=True)
	""" not uploading images in dev else make False to True"""
	photo = models.ImageField(upload_to='Registered_folks',blank=False)

	date = models.DateTimeField(auto_now=True)

