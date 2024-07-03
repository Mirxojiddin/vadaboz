from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Manager


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
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
	user_photo = models.ImageField(default="default_photo.jpg")

	def clean(self):
		super().clean()
		if self.district and self.province and self.district.province != self.province:
			raise ValidationError('The district must belong to the selected province.')
		if self.city:
			if not self.province or not self.district:
				raise ValidationError('Both province and district must be selected for the city.')
			if self.city.district != self.district or self.city.province != self.province:
				raise ValidationError('The city must belong to the selected district and province.')

	def __str__(self):
		return self.username

	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"


class FriendRequest(models.Model):
	from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
	to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user')
	status = models.BooleanField(default=0)

	def __str__(self):
		return f"{self.from_user.first_name} {self.to_user.first_name}"


class UserFriend(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
	friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend')

	def __str__(self):
		return f"{self.friend.first_name} {self.user.first_name}"




