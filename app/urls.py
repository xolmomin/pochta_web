from django.urls import path

from app.views import admin, auth, client, moderator as mod

# auth
urlpatterns = [
    path('', auth.LoginView.as_view(), name='login_page'),
    path('logout', auth.LogoutView.as_view(), name='logout_page'),
]

# admin
urlpatterns += [
    path('admin/letter', admin.admin_letter, name='admin_letter_page'),
    path('admin/client', admin.admin_client, name='admin_client_page'),
    path('admin/staff', admin.admin_staff, name='admin_staff_page'),
    path('admin/report', admin.admin_report, name='admin_report_page'),
    path('admin/branch', admin.admin_create_branch, name='admin_create_branch_page'),
    path('admin/create-branch', admin.admin_branch, name='admin_branch_page'),
]

# client
urlpatterns += [
    path('client/letter', client.client_letter, name='client_letter_page'),
    path('client/new-letter', client.client_new_letter, name='client_new_letter_page'),
    path('client/create-letter', client.create_letter, name='client_create_letter_page'),
    path('client/report', client.client_report, name='client_report_page'),
]

# moderator
urlpatterns += [
    path('mod/letter', mod.moderator_letter, name='mod_letter_page'),
    path('mod/client', mod.moderator_client, name='mod_client_page'),
    path('mod/staff', mod.moderator_staff, name='mod_staff_page'),
    path('mod/report', mod.moderator_report, name='mod_report_page'),
]
