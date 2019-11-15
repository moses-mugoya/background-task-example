
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from background_task import background
from datetime import timedelta
import datetime

# Create your views here.
@background(schedule=datetime.datetime(2019, 11, 15, 13, 4))
def hello():
    print("Hello World!")

def index(request):
    return HttpResponse("Hello world !")

