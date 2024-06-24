from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf.views import LoadDistrictsView, LoadCitiesView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('ajax/load-districts/', LoadDistrictsView.as_view(), name='ajax_load_districts'),
    path('ajax/load-cities/', LoadCitiesView.as_view(), name='ajax_load_cities'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)