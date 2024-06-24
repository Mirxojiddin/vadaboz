
from django.contrib import admin
from django.urls import path, include

from conf.views import LoadDistrictsView, LoadCitiesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('ajax/load-districts/', LoadDistrictsView.as_view(), name='ajax_load_districts'),
    path('ajax/load-cities/', LoadCitiesView.as_view(), name='ajax_load_cities'),
]
