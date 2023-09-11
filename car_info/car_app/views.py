from django.shortcuts import render, redirect
from .models import Car


def car_form(request):
    if request.method == 'POST':
        make = request.POST['make']
        year = request.POST['year']
        color = request.POST['color']
        mileage = request.POST['mileage']
        price = request.POST['price']
        Car.objects.create(make=make, year=year, color=color, mileage=mileage, price=price)
        return redirect('car_list')

    return render(request, 'car_app/car_form.html')


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_app/car_list.html', {'cars': cars})
