from django.shortcuts import redirect, render
from django.views.generic import View


class LoginView(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'app/auth.html')

    def post(self, *args, **kwargs):
        return render(self.request, 'app/auth.html')


class ModeratorView(View):
    pass


class ClientView(View):
    pass


class AdminView(View):
    pass
