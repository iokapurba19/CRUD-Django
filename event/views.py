from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

# Create your views here.
# CREATE
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    # fields = ['title', 'description', 'date', 'location']
    template_name = 'event-form.html'
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Event'
        return context

# READ
class EventListView(ListView):
    model = Event
    template_name = 'event-list.html'
    context_object_name = 'event_list' # Nama variabel untuk digunakan di template

# UPDATE
class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']
    template_name = 'event-form.html'
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Event'
        return context

# DELETE
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event-confirm-delete.html'
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Event'
        return context