from django import forms

from promise.models import Promise


class PromiseCreateForm(forms.ModelForm):
	class Meta:
		model = Promise
		fields = ('title', 'body', 'public', 'finished_at')


class PromiseUpdateForm(forms.ModelForm):
	class Meta:
		model = Promise
		fields = ['title', 'body', 'status', 'finished_at', 'public']
