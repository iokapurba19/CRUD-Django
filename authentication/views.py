# views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

class LoginFormView(LoginView):
    template_name = 'login.html'  # Lokasi template login
    redirect_authenticated_user = True  # Jika user sudah login, arahkan ke halaman lain

    def form_valid(self, form):
        messages.success(self.request, 'You were successfully logged in')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

class LogoutFormView(LogoutView):
    next_page = reverse_lazy('authentication:login')  # URL tujuan setelah logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You were successfully logged out')
        return super().dispatch(request, *args, **kwargs)
