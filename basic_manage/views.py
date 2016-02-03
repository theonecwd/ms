from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template import Context ,RequestContext
from django.contrib.auth.models import User

from models import *
from system_manage.models import * 
from django.contrib.auth.decorators import login_required
import shutil
import cv
import time
# Create your views here.


def add_device(request):
    return render_to_response('add_device.html',content,context_instance=RequestContext(request))
