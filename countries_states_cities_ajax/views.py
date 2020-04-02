from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from countries_states_cities_ajax.models import Country, State, City


def indexView(request):
    return render(request, 'index.html')


def viewCountries(request):
    if request.is_ajax and request.method == 'GET':
        countries = Country.objects.all().order_by('country_name')
        json_countries = serializers.serialize("json", countries)
    return JsonResponse({"countries": json_countries}, status=200)


def viewStatesByCountry(request):
    if request.is_ajax and request.method == 'GET':
        country_id = request.GET.get('countryId')
        states = State.objects.filter(country_id=country_id).order_by('state_name')
        json_states = serializers.serialize("json", states)
    return JsonResponse({"states": json_states}, status=200)


def viewCitiesByState(request):
    if request.is_ajax and request.method == 'GET':
        state_id = request.GET.get('stateId')
        cities = City.objects.filter(state_id=state_id).order_by('city_name')
        json_cities = serializers.serialize("json", cities)
    return JsonResponse({"cities": json_cities}, status=200)
