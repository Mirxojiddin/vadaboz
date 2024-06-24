from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from accounts.form import  CustomUserRegistrationForm, CustomUserUpdateForm
from accounts.models import District, City


class RegisterView(View):

    def get(self, request):
        create_form = CustomUserRegistrationForm
        contex = {
            'form': create_form
        }
        return render(request, 'accounts/register.html', contex)

    def post(self, request):
        create_form = CustomUserRegistrationForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.info(request, "tabriklaymiz")
            return redirect('users:login')
        else:
            contex = {
                'form': create_form
            }
            return render(request, 'accounts/register.html', contex)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm
        contex = {
            'form': login_form
        }
        return render(request, 'accounts/login.html', contex)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga kirdingiz")
            return redirect("index")
        else:
            return render(request, 'accounts/login.html', {"form": login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan chiqtingiz")
        return redirect("index")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, "accounts/profile.html", {"user": user})


class ProfileEdit(LoginRequiredMixin, View):
    def get(self, request):
        edit_form = CustomUserUpdateForm(instance=request.user)
        contex = {
            'form': edit_form
        }
        return render(request, 'accounts/profile_edit.html', contex)

    def post(self, request):
        edit_form = CustomUserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if edit_form.is_valid():
            edit_form.save()
            messages.info(request, "Ma'lumotlar muofiqaiyatli yangilandi")
            return redirect('users:profile')

        return render(request, "accounts/profile_edit.html", {"form": edit_form})


