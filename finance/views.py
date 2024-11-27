from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def capital(request):
    return HttpResponse('<h1>Tata Capital Limited is a financial and investment service provider in India. The company is based in Mumbai and has more than 700 branches across the country.</h1>')

def mutualfund(request):
    return HttpResponse('<h1>We are a part of the Tata group, one of India largest and most respected industrial groups, renowned for its adherence to business ethics. The Group has always believed in returning wealth to the society that it serves.</h1>')
