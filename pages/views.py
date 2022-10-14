from django.shortcuts import render
from cars.models import Car
from cars.views import search
from pages.models import Teams
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(latest_cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    #search_fields = Car.objects.values('model','city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'featured_cars': featured_cars,
        'latest_cars': paged_cars,
       # 'search_fields': search_fields
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search

    }
    return render(request,'pages/home.html', data)

def about(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams,
    }
    return render(request,'pages/about.html', data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')