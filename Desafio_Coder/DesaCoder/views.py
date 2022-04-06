from django.shortcuts import render
from DesaCoder.models import Familia
# Create your views here.

from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template,Context, loader
from datetime import datetime


def primer_vista(request):
    familiares=Familia.objects.all()
    return render(request,"inicio.html",{"familiares":familiares})