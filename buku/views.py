from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Buku

class BukuListView(LoginRequiredMixin, ListView):
    model = Buku
    template_name = 'buku_list.html'
    context_object_name = 'buku_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daftar Buku'
        return context

class BukuCreateView(LoginRequiredMixin, CreateView):
    model = Buku
    template_name = 'buku_form.html'
    fields = ['judul', 'penulis', 'penerbit', 'tahun_terbit', 'harga', 'stok']
    success_url = reverse_lazy('buku:buku-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Buku'
        return context
        
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

class BukuUpdateView(LoginRequiredMixin, UpdateView):
    model = Buku
    template_name = 'buku_form.html'
    fields = ['judul', 'penulis', 'penerbit', 'tahun_terbit', 'harga', 'stok']
    success_url = reverse_lazy('buku:buku-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Buku'
        return context
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

class BukuDeleteView(LoginRequiredMixin, DeleteView):
    model = Buku
    template_name = 'buku_confirm_delete.html'
    success_url = reverse_lazy('buku:buku-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hapus Buku'
        return context
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

class BukuDetailView(LoginRequiredMixin, DetailView):
    model = Buku
    template_name = 'buku_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Buku'
        return context