# from datetime import datetime
# from random import randint
#
# from django.contrib.auth.hashers import make_password
# from django_filters import rest_framework as filters
# from rest_framework import permissions, generics, status
# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.compat import coreapi, coreschema
# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.response import Response
# from rest_framework.schemas import ManualSchema, coreapi as coreapi_schema
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet, GenericViewSet
#
# from app.api import serializers
# from app.models import Staff, Letter, District, Region, Massive
#
#
# class StaffModelViewSet(ModelViewSet):
#     queryset = Staff.objects.filter(role=Staff.STAFF)  # Xodim
#     serializer_class = serializers.StaffSerializer
#     http_method_names = ['get']
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fields = {
#         'role': ['exact'],
#     }
#
#     def get_queryset(self):
#         query = super().get_queryset()
#         if self.request.user.is_authenticated:
#             if self.request.user.role == Staff.MODERATOR:
#                 return query.filter(region=self.request.user.region)
#         return query
#
#
# class ClientModelViewSet(ModelViewSet):
#     queryset = Staff.objects.filter(role=Staff.CLIENT)  # Klient
#     serializer_class = serializers.ClientSerializer
#     http_method_names = ['get']
#
#     def get_queryset(self):
#         query = super().get_queryset()
#         if self.request.user.is_authenticated:
#             if self.request.user.role == Staff.MODERATOR:
#                 return query.filter(region=self.request.user.region)
#         return query
#
#
# class LetterModelViewSet(ModelViewSet):
#     queryset = Letter.objects.all()
#     serializer_class = serializers.LetterSerializer
#
#     @action(methods=['get'], detail=False)
#     def own(self, request, *args, **kwargs):
#         user = request.user
#         letters = Letter.objects.filter(client=user)
#         letter_serializer = serializers.LetterSerializer(letters, many=True)
#         return Response(letter_serializer.data)
#
#     @action(methods=['get'], detail=False)
#     def branch_letter(self, request, *args, **kwargs):
#         user = request.user
#         letters = Letter.objects.filter(client__branch=user)
#         letter_serializer = serializers.LetterSerializer(letters, many=True)
#         return Response(letter_serializer.data)
#
#
# class RegionModelViewSet(ModelViewSet):
#     queryset = Region.objects.all()
#     serializer_class = serializers.CustomRegionSerializer
#     http_method_names = ['get']
#
#     def list(self, request, *args, **kwargs):
#         regions = Region.objects.all()
#         result = {}
#         for region in regions:
#             district_list = [district[0] for district in District.objects.values_list('name')] \
#                 if region.name == "hammasi" \
#                 else [district[0] for district in
#                       District.objects.filter(region__name=region.name).values_list('name')]
#
#             result[region.name] = district_list
#         return Response(result)
#
#
# class DistrictModelViewSet(ModelViewSet):
#     queryset = District.objects.all()
#     serializer_class = serializers.DistrictSerializer
#     http_method_names = ['get']
#
#
# class MassiveModelViewSet(ModelViewSet):
#     queryset = Massive.objects.all()
#     serializer_class = serializers.MassiveSerializer
#     http_method_names = ['get']
#
#
# class CustomObtainAuthToken(ObtainAuthToken):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = serializers.CustomAuthTokenSerializer
#
#     if coreapi_schema.is_enabled():
#         schema = ManualSchema(
#             fields=[
#                 coreapi.Field(
#                     name="password",
#                     required=True,
#                     location='form',
#                     schema=coreschema.String(
#                         title="Password",
#                         description="Valid password for authentication",
#                     ),
#                 ),
#             ],
#             encoding="application/json",
#         )
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         serializer_user = serializers.StaffSerializer(user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'data': serializer_user.data}, status=200)
#
#
# class BranchCreateAPIView(generics.CreateAPIView):
#     queryset = Staff.objects.all()
#     serializer_class = serializers.AddBranchSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         fish = serializer.data.get('fish', None)
#         phone = serializer.data.get('phone', None)
#         region = serializer.data.get('region', None)
#         address = serializer.data.get('address', None)
#         email = serializer.data.get('email', None)
#         username = serializer.data.get('username', None)
#         password = serializer.data.get('password', None)
#
#         region = Region.objects.filter(name__contains=region).first()
#         if Staff.objects.filter(username=username).exists():
#             raise ValidationError("username is already exists")
#         staff = Staff.objects.create(
#             name=fish,
#             phone=phone,
#             region=region,
#             email=email,
#             address=address,
#             username=username,
#             password=make_password(password),
#             role=Staff.MODERATOR  # Xodim
#         )
#
#         return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
#
#
# class StaffCreateAPIView(generics.CreateAPIView):
#     queryset = Staff.objects.all()
#     serializer_class = serializers.AddStaffSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         fish = serializer.data.get('fish', None)
#         phone = serializer.data.get('phone', None)
#         region_name = serializer.data.get('region', None)
#         branch = request.data.get('branch')
#         address = serializer.data.get('address', None)
#         passport_number = serializer.data.get('passport_number', None)
#         passport_give_date = serializer.data.get('passport_give_date', None)
#         given_by_whom = serializer.data.get('given_by_whom', None)
#         username = serializer.data.get('username', None)
#         password = serializer.data.get('password', None)
#         if branch:
#             split_branch = branch.split('|')
#             branch = Staff.objects.filter(name=split_branch[0], region__name=split_branch[1]).first()
#         else:
#             raise ValidationError("Filial topilmadi !")
#
#         region = Region.objects.filter(name=region_name).first()
#
#         if Staff.objects.filter(username=username).exists():
#             raise ValidationError("bunday login bor")
#
#         staff = Staff.objects.create(
#             name=fish,
#             phone=phone,
#             region=Region.objects.filter(name__contains=region).first(),
#             address=address,
#             branch=branch,
#             passport_number=passport_number,
#             passport_give_date=datetime.strptime(passport_give_date, "%d-%m-%Y").date(),
#             given_by_whom=given_by_whom,
#             username=username,
#             password=make_password(password),
#             role=Staff.STAFF  # Xodim
#         )
#
#         return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
#
#
# class ClientCreateAPIView(generics.CreateAPIView):
#     queryset = Staff.objects.all()
#     serializer_class = serializers.AddClientSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         fish = serializer.data.get('fish', None)
#         company = serializer.data.get('company', None)
#         inn = serializer.data.get('inn', None)
#         r_s = serializer.data.get('r_s', None)
#         bank = serializer.data.get('bank', None)
#         mfo = serializer.data.get('mfo', None)
#         branch = serializer.data.get('branch', None)
#
#         phone = serializer.data.get('phone', None)
#         region_name = serializer.data.get('region', None)
#         region = Region.objects.filter(name=region_name).first()
#         district = serializer.data.get('district', None)
#         address = serializer.data.get('address', None)
#         username = serializer.data.get('username', None)
#         if Staff.objects.filter(username=username).exists():
#             raise ValidationError("username is already exists")
#         password = serializer.data.get('password', None)
#         email = serializer.data.get('email', None)
#
#         if branch:
#             split_branch = branch.split('|')
#             branch = Staff.objects.filter(name=split_branch[0], region__name=split_branch[1]).first()
#         else:
#             raise ValidationError("Filial topilmadi !")
#
#         region = Region.objects.filter(name__contains=region).first()
#         if not region:
#             raise ValidationError("Viloyat topilmadi !")
#
#         district = Region.objects.filter(name__contains=district).first()
#
#         staff = Staff.objects.create(
#             name=fish,
#             company=company,
#             inn=inn,
#             phone=phone,
#             r_s=r_s,
#             bank=bank,
#             branch=branch,
#             mfo=mfo,
#             region=region,
#             district=district,
#             address=address,
#             username=username,
#             password=make_password(password),
#             email=email,
#             role=Staff.CLIENT  # Client
#         )
#         return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
#
#
# class CurierLetterListAPIView(generics.ListAPIView):
#     queryset = Letter.objects.all()
#     serializer_class = serializers.LetterSerializer
#
#     def list(self, request, *args, **kwargs):
#         user = request.user
#         if user.is_authenticated:
#             queryset = Letter.objects.filter(curier=user)
#         else:
#             queryset = Letter.objects.all()
#         queryset = self.filter_queryset(queryset)
#
#         # page = self.paginate_queryset(queryset)
#         # if page is not None:
#         #     serializer = self.get_serializer(page, many=True)
#         #     return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class CheckBarcodeAPIView(APIView):
#
#     def get(self, request, format=None):
#         barcode = request.query_params.get('barcode', None)
#         if Letter.objects.filter(barcode=barcode).exists():
#             letter = Letter.objects.get(barcode=barcode)
#             data = serializers.LetterSerializer(letter).data
#             return Response(data)
#         return Response("Bunday shtrix kod yoq!", 404)
#
#
# class ReportPageAPIView(GenericViewSet):
#     def get(self, request, *args, **kwargs):
#         before = request.query_params.get('before', None)
#         after = request.query_params.get('after', None)
#         user = request.user
#         queryset = Letter.objects.filter(curier=user)
#         if before:
#             queryset = queryset.filter(created_at__lte=before)
#         if after:
#             queryset = queryset.filter(created_at__gte=after)
#         return Response(queryset.count())
#
#
# class GenerateBarcodeAPIView(generics.RetrieveAPIView):
#     queryset = Letter.objects.all()
#     serializer_class = serializers.LetterPostSerializer
#
#     def generate_number(self, prefix_num):
#         def finalize(nums):
#             check_sum = 0
#             check_offset = (len(nums) + 1) % 2
#
#             for i, num in enumerate(nums):
#                 if (i + check_offset) % 2 == 0:
#                     n_ = num * 2
#                     check_sum += n_ - 9 if n_ > 9 else n_
#                 else:
#                     check_sum += num
#             return nums + [10 - (check_sum % 10)]
#
#         so_far = prefix_num + [randint(1, 9) for x in range(13)]
#         card_number = "".join(map(str, finalize(so_far)))[:12]
#
#         return card_number
#
#     def get(self, request, *args, **kwargs):
#         code = request.user.region.code
#         Letter.objects.filter()
#         while 1:
#             barcode = self.generate_number([int(i) for i in str(code)])
#             if not Letter.objects.filter(barcode=barcode).exists():
#                 break
#         return Response({"barcode": barcode})
#
#
# class LetterCreateAPIView(generics.CreateAPIView):
#     queryset = Letter.objects.all()
#     serializer_class = serializers.LetterPostSerializer
#
#     def create(self, request, *args, **kwargs):
#         region_name = request.data.get('region')
#         data = request.data.copy()
#         if not Region.objects.filter(name=region_name).exists():
#             raise ValidationError('Viloyat nomi xato!')
#         region = Region.objects.get(name=region_name)
#         data['region'] = region.id
#
#         district_name = request.data.get('district')
#         if not District.objects.filter(name=district_name).exists():
#             raise ValidationError('Tuman nomi xato!')
#         district = District.objects.get(name=district_name)
#         data['district'] = district.id
#         data['client'] = request.user.id
#
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# class LetterRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Letter.objects.all()
#     serializer_class = serializers.LetterDataSerializer
#
#
# class BranchListAPIView(generics.ListAPIView):
#     queryset = Staff.objects.filter(role=Staff.MODERATOR)
#     serializer_class = serializers.GetBranchSerializer
#
#
# class ClientReportListAPIView(generics.ListAPIView):
#     queryset = Staff.objects.filter(role=Staff.CLIENT)
#     serializer_class = serializers.ClientReportSerializer
#
#     # def list(self, request, *args, **kwargs):
#     #     queryset = self.filter_queryset(self.get_queryset())
#     #
#     #     page = self.paginate_queryset(queryset)
#     #     if page is not None:
#     #         serializer = self.get_serializer(page, many=True)
#     #         return self.get_paginated_response(serializer.data)
#     #
#     #     serializer = self.get_serializer(queryset, many=True)
#     #     return Response(serializer.data)
