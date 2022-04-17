from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

# from app.api.views import CustomObtainAuthToken
from core import settings

urlpatterns = [
  path('master-admin/', admin.site.urls),
  path('', include('app.urls')),
  path('api/v1/', include('app.api.urls')),
  # path('api/auth/', CustomObtainAuthToken.as_view()),
  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
