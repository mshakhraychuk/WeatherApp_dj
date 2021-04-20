import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


def index(request):
    key = '9adaa09047557e91e33f881d8de28019'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'id': city.id,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def delete_city(request, id):
    city_card = City.objects.get(id=id)
    city_card.delete()
    return redirect(index)
