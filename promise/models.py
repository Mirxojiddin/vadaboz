from django.db import models

from accounts.models import CustomUser


class Promise(models.Model):
	STATUS_CHOICES = [
		('not start', 'NOT START'),
		('in progress', 'IN PROGRESS'),
		('finished', 'FINISHED'),
		('failed', 'FAILED'),

	]
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	status = models.CharField(default='not start', max_length=12, choices=STATUS_CHOICES)
	created_at = models.DateField(auto_now=True)
	finished_at = models.DateField(null=True, blank=True)
	public = models.BooleanField(default=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.title}, {self.user.first_name}"


class BrokenPromise(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	promise = models.ForeignKey(Promise, on_delete=models.CASCADE)
	cause = models.TextField()
	created_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		unique_together = ('user', 'promise')

	def __str__(self):
		return f"{self.promise.__str__()}"


class FinishedPromise(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	promise = models.ForeignKey(Promise, on_delete=models.CASCADE)
	proof = models.TextField()
	href = models.CharField(max_length=200)
	created_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		unique_together = ('user', 'promise')

	def __str__(self):
		return f"{self.promise.__str__()}"
