from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def airasia(request):
    return HttpResponse('<h1>AIX Connect, formerly known as AirAsia India, was an Indian low-cost airline headquartered in Bangalore (Bengaluru), Karnataka and a wholly-owned subsidiary of Air India Limited which in turn is owned by Tata Group.</h1>')

def vistara(request):
    return HttpResponse('<h1>Tata SIA Airlines Limited (d/b/a Vistara) was an Indian full-service airline, based in Gurgaon, with its hub at Indira Gandhi International Airport. </h1>')