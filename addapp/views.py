from django.shortcuts import render,render_to_response
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Create your views here.
  

def address(request):
	return render(request, 'address.html')
def show(request):
	address = request.POST.get("address")
	print request.POST.get("address")
	geolocator = Nominatim()
	location = geolocator.geocode(request.POST.get("address"))
	# print(location.address)
	# print((location.latitude, location.longitude))
	return render(request,'test.html',{'data':[request.POST.get("address"),location.latitude, location.longitude]})
