from django.urls import path
from .views import (
    BukuListView,
    BukuCreateView,
    BukuUpdateView,
    BukuDeleteView,
    BukuDetailView
)

urlpatterns = [
    path('', BukuListView.as_view(), name='buku-list'),
    path('tambah/', BukuCreateView.as_view(), name='buku-create'),
    path('<int:pk>/edit/', BukuUpdateView.as_view(), name='buku-update'),
    path('<int:pk>/hapus/', BukuDeleteView.as_view(), name='buku-delete'),
    path('<int:pk>/detail/', BukuDetailView.as_view(), name='buku-detail'),
] 
