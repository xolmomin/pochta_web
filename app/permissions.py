from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import redirect

from app.models import Staff


class IsAdminMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == Staff.ADMIN:
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class IsClientMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == Staff.CLIENT:
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class IsModeratorMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == Staff.MODERATOR:
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)
