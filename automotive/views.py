from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def motors(request):
    return HttpResponse('<h1>Tata Motors Limited is an Indian multinational automotive company, headquartered in Mumbai and part of the Tata Group. The company produces cars, trucks, vans, and buses.</h1>')

def jaguar(request):
    return HttpResponse('<h1>Jaguar is the sports car and luxury vehicle brand of Jaguar, which is under TATA Groups.</h1>')