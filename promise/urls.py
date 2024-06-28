from django.urls import path
from promise.views import PromiseView, PromiseDetailView, PromiseEditView,ConfirmDeletePromiseView,DeletePromiseView

app_name = 'promise'

urlpatterns =[
	path('', PromiseView.as_view(), name='promise_list'),
	path('<int:pk>', PromiseDetailView.as_view(), name='detail'),
	path('<int:pk>/edit/', PromiseEditView.as_view(), name='update'),
	path('<int:pk>/delete', DeletePromiseView.as_view(), name='delete'),
	path('<int:pk>/delete/confirm', ConfirmDeletePromiseView.as_view(), name='confirm-delete')
]