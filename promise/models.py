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
	status = models.CharField(default='not start', max_length=20, choices=STATUS_CHOICES)
	created_at = models.DateField(auto_now=True)
	finished_at = models.DateField(null=True)
	public = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.title}, {self.user.get_full_name}"
