from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from accounts.form import CustomUserRegistrationForm, CustomUserUpdateForm
from accounts.models import CustomUser, FriendRequest, UserFriend


class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        create_form = CustomUserRegistrationForm
        contex = {
            'form': create_form
        }
        return render(request, 'accounts/register.html', contex)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        create_form = CustomUserRegistrationForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.info(request, "tabriklaymiz")
            return redirect('accounts:login')
        else:
            contex = {
                'form': create_form
            }
            return render(request, 'accounts/register.html', contex)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        login_form = AuthenticationForm
        contex = {
            'form': login_form
        }
        return render(request, 'accounts/login.html', contex)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
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
            return redirect('accounts:profile')

        return render(request, "accounts/profile_edit.html", {"form": edit_form})


class FriendRequestView(View):
    def get(self, request, userid):
        friend = CustomUser.objects.get(id=userid)
        user = request.user
        FriendRequest.objects.create(from_user=user, to_user=friend)

        return redirect(reverse("accounts:familiar" ))


class FriendView(View):
    def get(self, request):
        friend_requests = FriendRequest.objects.filter(to_user=request.user.id)
        friends = UserFriend.objects.filter(Q(user=request.user.id) | Q(friend=request.user.id))
        return render(request, "accounts/friend.html", {"friend_requests": friend_requests, "friends": friends})


class AddFriendView(View):
    def get(self, request, id):
        friend = CustomUser.objects.get(id=id)
        user = request.user
        UserFriend.objects.create(friend=friend, user=user)
        FriendRequest.objects.get(to_user=user.id, from_user=friend.id).delete()
        return redirect("accounts:friends")


class RejectFriendView(View):
    def get(self, request, id):
        friend = CustomUser.objects.get(id=id)
        user = request.user
        FriendRequest.objects.filter(to_user=user.id, from_user=friend.id).delete()
        return redirect("accounts:friends")


class FriendDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend = CustomUser.objects.get(id=id)
        return render(request, "accounts/friend_detail.html", {"friend": friend})


class FamiliarUsersView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        users = CustomUser.objects.filter(
                                        Q(city=request.user.city) |
                                        Q(district=request.user.district) |
                                        Q(province=request.user.province)
                                           )
        friend_requests = FriendRequest.objects.filter(from_user=request.user.id)
        friends = UserFriend.objects.filter(Q(user=request.user.id) | Q(friend=request.user.id))
        id_friend = [user['user_id'] for user in friends.values()]
        id_request = [user['to_user_id'] for user in friend_requests.values()]
        contex = {

            'id_request': id_request,
            'id_friend': id_friend,
            "users": users
        }
        print(id_friend, id_request)

        return render(request, "accounts/family_users.html", contex )

