from django.urls import path
from .views import index, tambah_user, post_user, master_user, update_user, postupdate_user
# from . import views 

urlpatterns = [
    path('index', index, name='index'),
    path('tambah_user', tambah_user, name='tambahuser'),
    path('post_user', post_user, name='postuser'),
    
    #MAU NAMPLIN MODEL CRUD
    path('master_user', master_user, name='masteruser'),

    #UPDATE
    path('update_user/<str:userid>', update_user, name='updateuser'),
    path('postupdate_user', postupdate_user, name='postupdateuser')
]