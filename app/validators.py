from django.core.exceptions import ValidationError


def validate_phone(phone_number):
    # 998905002030

    if not (len(phone_number) == 12 and phone_number.isdigit() and phone_number.startswith('998')):
        raise ValidationError(
            "Telefon number to'g'ri emas, bunday formatda kiriting (991112233)",
            params={
                'value': phone_number
            },
        )
