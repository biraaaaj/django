from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
     }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights = flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        print(passenger_id)
        passenger = Passenger.objects.get(pk = passenger_id)
        print(passenger)
        flight = Flight.objects.get(pk = flight_id)
        print(flight_id)
        print(flight)
    except KeyError:
         return render(request,"flights/error.html",{"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request,"flights/error.html",{"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request,"flights/error.html",{"message": "No Passenger."})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args =(flight_id,)))
