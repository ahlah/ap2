from re import S
from django.shortcuts import redirect, render
from django.views import View

from .models import Hotel
from .forms import  SearchForm

import string

class IndexView(View):

    def get(self, request):
        hotels = Hotel.objects.all()
        context = {
            'hotels': hotels
        }
        return render(request, 'search/index.html', context)

class SearchView(View):

    def get(self, request):
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            sort = form.cleaned_data['sort']
            hotels = Hotel.objects.none()

            for keyword in query.split():
                hotels = hotels.union(Hotel.objects.filter(title__icontains=keyword))
                hotels = hotels.union(Hotel.objects.filter(description__icontains=keyword))
                hotels = hotels.union(Hotel.objects.filter(city__icontains=keyword))
                hotels = hotels.union(Hotel.objects.filter(country__icontains=keyword))

            if sort == "pa":
                hotels = hotels.order_by("price")
            elif sort == "pd":
                hotels = hotels.order_by("-price")
            elif sort == "ra":
                hotels = hotels.order_by("rating")
            elif sort == "rd":
                hotels = hotels.order_by("-rating")
            
            context = {
                'query': query,
                'sort': sort,
                'hotels': hotels
            }
        else:
            context = {}
        return render(request, 'search/search.html', context)



