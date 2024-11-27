from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tcs(request):
    return HttpResponse('<h1>Tata Consultancy Services is an Indian multinational technology company specializing in information technology services and consulting. Headquartered in Mumbai, it is a part of the Tata Group and operates in 150 locations across 46 countries.</h1>')
def tcsion(request):
    return HttpResponse('<h1>TCS iON, a unit of Tata Consultancy Services, is focused on empowering people and organisations with tech-led solutions to transform the educational and skill development domains for the new world. We use a uniquely built ‘phygital’ platform that connects the digital and physical worlds.</h1>')