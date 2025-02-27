from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CRUD
from django.contrib import messages
from django.db.models import Q
import json

# Create your views here.
def index(request):
    context = {
        'name': 'Felice Sirait'
    }
    return render(request, 'index.html', context)

def tambah_user(request):
    return render(request, 'tambah-user.html')

def post_user(request):
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if CRUD.objects.filter(userid=userid).exists():
        messages.error(request, 'USERID SUDAH DIGUNAKAN')
    else :
        if password == password2:
            tambah_user = CRUD(
                userid=userid,
                username=username,
                password=password
            )
            tambah_user.save()
            messages.success(request, 'USER BERHASIL DITAMBAHKAN')
        else:
            messages.error(request, 'PASSWORD TIDAK SAMA')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def master_user(request):
    # MAU NAMPILIN DATA DARI MODEL CRUD
    # data_user = CRUD.objects.all().order_by('-userid')
    # data_user = CRUD.objects.filter(userid='1234')

    #pakai operator and 
    # data_user = CRUD.objects.filter(userid = '5678', username__icontains='jaka')

    #pakai operator or
    # data_user = CRUD.objects.filter(Q(userid = '5678') | Q(username__icontains='test'))

    # json_data_user= json.dumps(list(data_user.values()))
    # return HttpResponse(json_data_user)


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
    #mengambil data POST
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    #Proses Update
    user = CRUD.objects.get(userid=userid)
    if password == password2:
        user.username = username
        user.password = password
        user.save()
        messages.success(request, 'USER BERHASIL DIUPDATE')
    else:
         messages.error(request, 'PASSWORD TIDAK SAMA')

    return redirect(request.META.get('HTTP_REFERER', '/'))