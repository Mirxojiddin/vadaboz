from django import forms
from django.forms import DateInput
from promise.models import Promise, PromiseCommit


class PromiseCreateForm(forms.ModelForm):
	class Meta:
		model = Promise
		fields = ('title', 'body', 'public', 'finished_at')

	finished_at = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),  # HTML5 'date' input type
        required=False
    )


class PromiseUpdateForm(forms.ModelForm):
	class Meta:
		model = Promise
		fields = ['title', 'body', 'status', 'finished_at', 'public']
		
		finished_at = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),  # HTML5 'date' input type
        required=False
   		)


class PromiseCommitForm(forms.ModelForm):
	class Meta:
		model = PromiseCommit
		fields = ['commit']
