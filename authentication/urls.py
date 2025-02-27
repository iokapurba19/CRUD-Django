# authentication/urls.py
from django.urls import path
from .views import LoginFormView, LogoutFormView

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
]
