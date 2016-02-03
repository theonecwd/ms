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


def test(request):
    return HttpResponse ("hello world")


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index')
    state = ''

    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username= username ,password= password)
        if user and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/index')
        else:
            user=general_user.objects.filter(name__exact=username,password__exact =password)
            if user:
                return HttpResponseRedirect("/index?username=%s" % username)
    return render_to_response('login.html', context_instance=RequestContext(request))
                

def index(request):
    if request.user.is_authenticated():
        username =request.user.username
    elif request.GET['username']:
        username = request.GET['username']
    else:
        username = None
    content = {
            'user':username,
            }
    return render_to_response('index.html',content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def code(request):
    return render(request,'code.html')

def mainpage(request):
    #return render(request,'welcome.html')
    return render_to_response('mainpage.html')

def cwd(request):
    return render_to_response("cwd.html")


def form(request):
    state = ''
    if request.POST:
        name = request.POST.get('name','')
        age = request.POST.get('age','')
        if name and age:
            person = Person(name=name,age=age)
            person.save()
            state ='success'
        else :
            state = 'error'
    content = {
            'state':state,
            }

    return render_to_response('addCourse.html',content,context_instance = RequestContext(request))




def camera(request):
    cam = cv.CaptureFromCAM(-1)
    while True:
        cv.GrabFrame(cam)
        img = cv.RetrieveFrame(cam)
        cv.SaveImage("test.jpg", img)
        time.sleep(0.5)
        shutil.move("test.jpg","./static/test.jpg")
        return render_to_response('camera.html')



def system_manage(request):
    return HttpResponse("this is system_manage page")

def basic(request):
    return HttpResponse("this is basic page")

def emergence(request):
    return HttpResponse("this is emergence page")



def modify_password(request):
    state = ''
    print "hello"
    if request.POST:
        old_password = request.POST.get('old_password','')
        new_password1 = request.POST.get('new_password_1','')
        new_password2 = request.POST.get('new_password_2','')
        print old_password
        print new_password1
        state = 'error'
        if old_password and new_password1 and new_password2 :

            username = request.GET['username']
            print username
            user = general_user.objects.get(name=username)
            if user:
                print "find the general_user"
                user.password=new_password1
                user.save()
                state = 'success'
            else:
                user = auth.authenticate(username= username ,password=old_password)
                if user:
                    print "find the superuser"
                    user.password = new_password1
                    user.save()
                    state = 'success'
    content = {
            'state':state,
            }
    return render_to_response('modify_password.html', content, context_instance=RequestContext(request))
    #return render_to_response('test.html', content, context_instance=RequestContext(request))
    #return HttpResponse(username)
