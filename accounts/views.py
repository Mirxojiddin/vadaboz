from django.shortcuts import render
from django.views import View


class LoginView(View):
	def get(self, request):
		return render(request, 'accounts/login.html')

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

