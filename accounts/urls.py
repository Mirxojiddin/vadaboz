from django.urls import path

from accounts.views import LoginView, RegisterView, LogoutView, ProfileView, ProfileEdit, FriendView, FriendDetailView, \
	AddFriendView, RejectFriendView, FriendRequestView, FamiliarUsersView

app_name = 'accounts'

urlpatterns = [
	path('register', RegisterView.as_view(), name='register'),
	path('login', LoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('profile', ProfileView.as_view(), name='profile'),
	path('profile_edit', ProfileEdit.as_view(), name='profile_edit'),
	path('friends', FriendView.as_view(), name='friends'),
	path('friend-ditail/<int:id>', FriendDetailView.as_view(), name='friend-ditail'),
	path('add-friends/<int:id>', AddFriendView.as_view(), name='add-friend'),
	path('reject-friends/<int:id>', RejectFriendView.as_view(), name='reject-friend'),
	path('friend_request/<int:userid>', FriendRequestView.as_view(), name='friend-request'),
	path('familiar/', FamiliarUsersView.as_view(), name='familiar'),

]