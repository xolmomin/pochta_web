# from django.contrib.auth import authenticate
# from rest_framework import serializers
#
# from app import models
#
#
# class MassiveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Massive
#         fields = [
#             "id",
#             "name",
#             "district",
#         ]
#
#
# class DistrictSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.District
#         fields = [
#             "name",
#         ]
#
#
# class RegionWithNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Region
#         fields = [
#             "name",
#         ]
#
#
# class AddClientSerializer(serializers.Serializer):
#     fish = serializers.CharField(max_length=255)
#     company = serializers.CharField(max_length=255)
#     inn = serializers.CharField(max_length=255)
#     phone = serializers.CharField(max_length=255)
#     region = serializers.CharField(max_length=255)
#     branch = serializers.CharField(max_length=255)
#     district = serializers.CharField(max_length=255)
#     address = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#
#
# class AddStaffSerializer(serializers.Serializer):
#     fish = serializers.CharField(max_length=255)
#     phone = serializers.CharField(max_length=255)
#     region = serializers.CharField(max_length=255)
#     address = serializers.CharField(max_length=255)
#     passport_number = serializers.CharField(max_length=255)
#     passport_give_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
#     given_by_whom = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=255)
#
#
# class AddBranchSerializer(serializers.Serializer):
#     fish = serializers.CharField(max_length=255)
#     phone = serializers.CharField(max_length=255)
#     region = serializers.CharField(max_length=255)
#     address = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=255)
#
#
# class ClientReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Staff
#         fields = [
#             "id",
#             "company",
#             "get_letter_client_count",
#             "inn"
#         ]
#
#
# class GetBranchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Staff
#         fields = [
#             'id',
#             'name',
#             'phone',
#             'region',
#             'email',
#             'username',
#             'address',
#         ]
#
#     def to_representation(self, instance):
#         context = super().to_representation(instance)
#         context['region'] = models.Region.objects.get(pk=instance.region.pk).name
#         return context
#
#
# class LetterPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Letter
#         fields = [
#             "id",
#             "client",
#             "region",
#             "district",
#             "phone",
#             "company",
#             "name",
#             "address",
#             "barcode",
#             "letter_text",
#         ]
#
#
# class LetterDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Letter
#         fields = [
#             "client",
#             "region",
#             "district",
#             "curier",
#             "company",
#             "name",
#             "status",
#             "address",
#             "barcode",
#             "letter_text",
#             "delivered_at",
#             "curier_accepted_at",
#         ]
#
#
# # inn, firma, login
#
# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Staff
#         fields = [
#             "id",
#             "company",
#             "inn",
#             "phone",
#             "username",
#             "date_joined",
#         ]
#
#
# class StaffSerializer(serializers.ModelSerializer):
#     region = RegionWithNameSerializer()
#
#     class Meta:
#         model = models.Staff
#         fields = [
#             "id",
#             "name",
#             "role",
#             "username",
#             "region",
#             "phone",
#             "address",
#         ]
#
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         ret['letter_count'] = instance.get_letter_client_count
#         ret['region'] = instance.region.name
#         return ret
#
#
# class CustomRegionSerializer(serializers.ModelSerializer):
#     district = DistrictSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = models.Region
#         fields = [
#             "name",
#             "district"
#         ]
#
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         district_list = [district['name'] for district in ret['district']]
#         result = {}
#         result[ret['name']] = district_list
#         return result
#
#
# class LetterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Letter
#         fields = [
#             "id",
#             "company",
#             "barcode",
#             "region",
#             "district",
#             "letter_text",
#             "created_at",
#             "delivered_at",
#             "name",
#             "status",
#             "address",
#             "client",
#         ]
#
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         if instance.region:
#             ret['region'] = instance.region.name
#         ret['client'] = StaffSerializer(instance.client).data if instance.client else None
#         if instance.district:
#             ret['district'] = instance.district.name
#         return ret
#
#
# class CustomAuthTokenSerializer(serializers.Serializer):
#     phone = serializers.CharField(
#         max_length=9,
#         label="Phone format(991112233)",
#         style={'input_type': 'string'},
#         trim_whitespace=True,
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         style={'input_type': 'password'},
#         trim_whitespace=True,
#         write_only=True
#     )
#
#     # 935248052
#     def validate(self, attrs):
#         password = attrs.get('password')
#         phone = attrs.get('phone')
#         if phone and password:
#             user = authenticate(request=self.context.get('request'), username=phone, password=password)
#             if not user:
#                 msg = "Bunday user topilmadi, parolni tekshirib ko'ring"
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Must include "password".'
#             raise serializers.ValidationError(msg, code='authorization')
#
#         attrs['user'] = user
#         return attrs
