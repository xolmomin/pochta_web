from django.urls import path

from app.views import LoginView, ClientView, AdminView, ModeratorView

urlpatterns = [
    path('', LoginView.as_view(), name='login_page'),
    path('client', ClientView.as_view(), name='client_page'),
    path('admin', AdminView.as_view(), name='admin_page'),
    path('moderator', ModeratorView.as_view(), name='moderator_page'),
]
