from django.urls import path
from it.views import *

urlpatterns=[
    path('tcs/',tcs,name='tcs'),
    path('tcsion/',tcsion,name='tcsion'),
]