from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from accounts.models import District, City


class LoadDistrictsView(View):
    def get(self, request):
        province_id = request.GET.get('province_id')
        districts = District.objects.filter(province_id=province_id).order_by('name')
        return JsonResponse(list(districts.values('id', 'name')), safe=False)


class LoadCitiesView(View):
    def get(self, request):
        district_id = request.GET.get('district_id')
        cities = City.objects.filter(district_id=district_id).order_by('name')
        return JsonResponse(list(cities.values('id', 'name')), safe=False)


def index(request):

    return render(request, "index.html")
