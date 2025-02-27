from django.shortcuts import render, redirect
from .models import CRUD
from django.http import HttpResponse    
from django.contrib import messages
from .utilities import ppn11persen
import json

# Create your views here.
def index (request):
    nilai = 110000
    hasil = ppn11persen(nilai)
    return HttpResponse(hasil)

def tambah_user(request):
    return render(request, 'tambah-user.html')

def post_user(request):
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if CRUD.objects.filter(userid=userid).exists():
        messages.error(request, 'User ID already exists')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        if password == password2:
         tambah_user = CRUD(
            userid = userid,
            username = username,
            password = password,
         )
         tambah_user.save()
         messages.success(request, 'User has been added')
        else:
            messages.error(request, 'Password does not match')

    return redirect(request.META.get('HTTP_REFERER', '/'))


def master_user(request):
    data_user = CRUD.objects.all()
    context = {
        'data_user': data_user
    }
    return render(request, 'master-user.html', context)
    
def update_user(request, userid):
    data_user = CRUD.objects.get(userid=userid)
    context = { 
        'data_user': data_user
    }           
    return render(request, 'update-user.html', context) 

def postupdate_user(request):
    # ambil data post
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    # proses update
    user = CRUD.objects.get(userid = userid)
    if password == password2:
        user.username = username
        user.password = password
        user.save()
        messages.success(request, 'User has been updated')
    else :
        messages.error(request, 'Password does not match')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_user(request, userid):
    user = CRUD.objects.get(userid=userid).delete()
    messages.success(request, 'User has been deleted')
    return redirect(request.META.get('HTTP_REFERER', '/'))