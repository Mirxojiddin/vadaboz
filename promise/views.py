from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from promise.form import PromiseCreateForm, PromiseUpdateForm
from promise.models import Promise


class PromiseView(LoginRequiredMixin, View):

	def get(self, request):
		user = request.user
		form = PromiseCreateForm()
		promises = Promise.objects.filter(user=user)
		context = {
			'form': form,
			'promises': promises,

		}

		return render(request, 'promise/promises.html', context)

	def post(self, request):
		user = request.user
		form = PromiseCreateForm(request.POST)
		if form.is_valid():
			promise = form.save(commit=False)
			promise.user = user
			promise.save()
			return redirect('promise:promise_list')
		else:
			return render(request, 'promise/promises.html', {'form': form})


class PromiseDetailView(LoginRequiredMixin, View):
	def get(self, request, pk):
		user = request.user
		promise = Promise.objects.get(id=pk, user=user)
		return render(request, 'promise/promise_detail.html', {"promise": promise})


class PromiseEditView(LoginRequiredMixin, View):
	def get(self, request, pk):
		user = request.user
		promise = Promise.objects.get(id=pk, user=user)
		form = PromiseUpdateForm(instance=promise)
		return render(request, 'promise/promise_update.html', {'form': form})

	def post(self, request, pk):
		user = request.user
		promise = Promise.objects.get(id=pk, user=user)
		form = PromiseUpdateForm(request.POST, instance=promise)
		if form.is_valid():
			form.save()
			return redirect('promise:detail', pk=promise.pk)
		return render(request, 'promises/promise_update.html', {'form': form})


class ConfirmDeletePromiseView(LoginRequiredMixin, View):
	def get(self, request, pk):
		promise = Promise.objects.get(id=pk)

		return render(request, "promise/confirm_delete_promise.html", {"promise": promise})


class DeletePromiseView(LoginRequiredMixin, View):
	def get(self, request, pk):
		promise = Promise.objects.get(id=pk)
		promise.delete()
		messages.success(request, "Vadangiz o'chirildi")

		return redirect(reverse("promise:promise_list"))
