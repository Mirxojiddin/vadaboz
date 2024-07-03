from django.urls import path
from promise.views import PromiseView, PromiseDetailView, PromiseEditView,ConfirmDeletePromiseView,DeletePromiseView, \
	AddLikeView, AddDislikeView,AddCommitView

app_name = 'promise'

urlpatterns =[
	path('', PromiseView.as_view(), name='promise_list'),
	path('<int:pk>', PromiseDetailView.as_view(), name='detail'),
	path('<int:pk>/edit/', PromiseEditView.as_view(), name='update'),
	path('<int:pk>/delete', DeletePromiseView.as_view(), name='delete'),
	path('<int:pk>/delete/confirm', ConfirmDeletePromiseView.as_view(), name='confirm-delete'),
	path('<int:pk>/like', AddLikeView.as_view(), name='like-promise'),
	path('<int:pk>/dislike', AddDislikeView.as_view(), name='dislike-promise'),
	path('<int:pk>/commit', AddCommitView.as_view(), name='commit-promise')
]