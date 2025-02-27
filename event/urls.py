from django.urls import path
from .views import (
    EventCreateView, 
    EventListView, 
    EventUpdateView, 
    EventDeleteView
)

urlpatterns = [
    #READ
    path('', EventListView.as_view(), name='event-list'),
    #CREATE
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    #UPDATE
    path('event/update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    #DELETE
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
]