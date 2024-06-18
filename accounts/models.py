from django.contrib.auth.models import AbstractUser
from django.db import models


class Province(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class District(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey(Province, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class CustomUser(AbstractUser):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	city = models.ForeignKey(City, on_delete=models.CASCADE)

	def __str__(self):
		return self.name




