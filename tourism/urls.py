from django.urls import path
from tourism.views import *

urlpatterns=[
    path('airasia/',airasia,name='ariasia'),
    path('vistara/',vistara,name='vistara'),
]