from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import FormView

from app.forms import LoginForm
from app.models import Staff


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'app/auth.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.role == Staff.ADMIN:
                return redirect('admin_letter_page')
            if user.role == Staff.CLIENT:
                return redirect('client_new_letter_page')
            if user.role == Staff.MODERATOR:
                return redirect('mod_letter_page')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                if user.role == Staff.ADMIN:
                    return redirect('admin_letter_page')
                if user.role == Staff.CLIENT:
                    return redirect('client_new_letter_page')
                if user.role == Staff.MODERATOR:
                    return redirect('mod_letter_page')
            messages.add_message(self.request, messages.WARNING, "Bu foydalanuvchiga rol berilmagan")
            return redirect('login_page')
        else:
            messages.add_message(self.request, messages.WARNING, "xatolik")
            return redirect('login_page')


class LogoutView(LoginRequiredMixin, generic.View):
    login_url = 'login_page'

    def get(self, request):
        logout(request)
        return redirect('login_page')
