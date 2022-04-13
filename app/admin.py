from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

from app import models


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        "phone",
    ]


class StaffProxy(models.Staff):
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        proxy = True


class ClientProxy(models.Staff):
    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klientlar"
        proxy = True


class ReportProxy(models.Staff):
    class Meta:
        verbose_name = "Xisobot"
        verbose_name_plural = "Xisobotlar"
        proxy = True


class BranchProxy(models.Staff):
    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"
        proxy = True


@admin.register(ReportProxy)
class StaffProxyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        "get_letter_count_admin",
        'inn',
    ]
    fields = [
        'company',
        'inn',
    ]

    def get_letter_count_admin(self, obj):
        return obj.get_letter_client_count

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=models.Staff.STAFF)  # Xodimlar

    get_letter_count_admin.short_description = 'xatlar soni'


@admin.register(StaffProxy)
class StaffProxyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        "phone",
    ]
    fields = [
        'name',
        'phone',
        'address',
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=models.Staff.STAFF)  # Xodimlar


@admin.register(BranchProxy)
class BranchProxyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'company',
        # 'region_name',
        # 'district_name',
        'date_joined',
    ]
    fields = [
        'id',
        'username',
        'company',
        # 'region_name',
        # 'district_name',
        'date_joined',
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=models.Staff.MODERATOR)  # Xodimlar


@admin.register(ClientProxy)
class ClientProxyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'inn',
        'phone',
        'username',
        'date_joined',
    ]
    fields = [
        'id',
        'company',
        'inn',
        'phone',
        'username',
        'date_joined',
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=models.Staff.CLIENT)


@admin.register(models.Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "region",
        "district",
        "delivered_at",
        "name",
        "status",
        "company",
        "created_at",
    ]


@admin.register(models.Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(models.District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'name',
        'region',
    ]


@admin.register(models.Massive)
class MassiveAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'district',
    ]


admin.site.unregister(Group)
