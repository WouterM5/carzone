from django.shortcuts import render
from cars.models import Car
from pages.models import Teams

# Create your views here.

def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    data = {
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
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