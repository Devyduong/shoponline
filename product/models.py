from django.db import models


class Category(models.Model):
	title = models.CharField(default = '', max_length=255)
	slug = models.CharField(max_length=200, default='')
	description = models.TextField(default='')
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(default = '', max_length=255)
	description = models.TextField(default='')
	avatar = models.ImageField(default='')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.FloatField(default=0)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

class Variation(models.Model):
	title = models.CharField(default = '', max_length=255)
	description = models.TextField(default='')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.FloatField(default=0)
	inventory = models.IntegerField(default=0)
	active = models.BooleanField(default=True)
		