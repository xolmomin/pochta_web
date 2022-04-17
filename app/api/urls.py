# from django.urls import path, include
# from rest_framework import routers
#
# from app.api import views
#
# router = routers.DefaultRouter()
# router.register("staff", views.StaffModelViewSet)
# router.register("client", views.ClientModelViewSet)
# router.register("letter", views.LetterModelViewSet)
# router.register("region", views.RegionModelViewSet)
# router.register("district", views.DistrictModelViewSet)
# router.register("massive", views.MassiveModelViewSet)
#
# # API urls
urlpatterns = [
#     path("", include(router.urls)),
#     path("client-add", views.ClientCreateAPIView.as_view()),  # desktop
#     path("staff-add", views.StaffCreateAPIView.as_view()),  # desktop
#     path("branch-add", views.BranchCreateAPIView.as_view()),  # desktop
#     path("client-report", views.ClientReportListAPIView.as_view()),  # desktop
#     path("get-branch", views.BranchListAPIView.as_view()),  # desktop
#     path("get-letter/<int:pk>", views.LetterRetrieveAPIView.as_view()),  # desktop
#     path("send-letter", views.LetterCreateAPIView.as_view()),  # desktop
#     path("generate-barcode", views.GenerateBarcodeAPIView.as_view()),  # desktop
#
#     path("curier-letters", views.CurierLetterListAPIView.as_view()),  # mobile
#     path("check-barcode", views.CheckBarcodeAPIView.as_view()),  # mobile
#     path("mobile-report-page", views.ReportPageAPIView.as_view({'get': 'get'})),  # mobile
]
