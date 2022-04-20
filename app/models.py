from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_integer
from django.db.models import (
    SmallIntegerField,
    Model,
    DateTimeField,
    CASCADE,
    ForeignKey,
    SET_NULL,
    CharField,
    DateField,
)


def get_directory(instance, filename):
    return 'letter/{0}-{1}'.format(instance.barcode, filename)


class Region(Model):  # Viloyat
    code = SmallIntegerField(default=0)
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"


class District(Model):  # Tuman
    region = ForeignKey(Region, CASCADE, 'district')

    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"


class Massive(Model):  # Massiv
    name = CharField(max_length=255)
    district = ForeignKey(District, CASCADE, 'massive')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Massiv"
        verbose_name_plural = "Massivlar"


class Letter(Model):
    STATUS = (
        ('new', 'yangi'),
        ('processing', 'yetkazilmoqda'),
        ('accepted', 'qabul qildi'),
        ('cancelled', 'qabul qilmadi'),
    )

    client = ForeignKey("app.Staff", SET_NULL, "letter_client", blank=True, null=True)
    region = ForeignKey("app.Region", SET_NULL, blank=True, null=True, verbose_name='Viloyat')
    district = ForeignKey("app.District", SET_NULL, blank=True, null=True, verbose_name='Tuman')
    currier = ForeignKey("app.Staff", SET_NULL, "letter_currier", blank=True, null=True)

    company = CharField(max_length=255, blank=True, null=True)
    name = CharField(max_length=255, blank=True, null=True, verbose_name='Nomi')
    status = CharField(max_length=20, choices=STATUS, default=STATUS[0][0])
    phone = CharField(max_length=25, blank=True, null=True, verbose_name='Telefon')
    address = CharField(max_length=255, blank=True, null=True, verbose_name='Manzil')
    barcode = CharField(max_length=12, blank=True, null=True)
    letter_text = RichTextUploadingField(null=True, blank=True, verbose_name='Xat')

    delivered_at = DateTimeField(blank=True, null=True)
    currier_accepted_at = DateTimeField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Xat"
        verbose_name_plural = "Xatlar"

    def __str__(self):
        return str(self.pk)

    def get_status(self):
        return dict(self.STATUS).get(self.status)


class Staff(AbstractUser):
    STAFF = 'staff'
    CLIENT = 'client'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    ROLE = (
        (STAFF, 'Xodim'),  # kuryer
        (CLIENT, 'Klient'),  # xat yoza oladigan odam
        (ADMIN, 'Admin'),  # eng katta admin
        (MODERATOR, 'Moderator'),  # filialdagi admin
    )
    branch = ForeignKey("self", SET_NULL, blank=True, null=True, verbose_name='Filial')
    region = ForeignKey("app.Region", SET_NULL, null=True, blank=True, verbose_name='Viloyat')
    district = ForeignKey("app.District", SET_NULL, null=True, blank=True, verbose_name='Tuman')

    name = CharField(max_length=255, verbose_name='FIO')
    company = CharField(max_length=255, blank=True, null=True)
    inn = CharField(max_length=100, blank=True, null=True, validators=[validate_integer])
    phone = CharField(max_length=15, null=True, blank=True, verbose_name='Telefon')
    address = CharField(max_length=255, blank=True, null=True, verbose_name='Manzil')
    role = CharField(max_length=15, choices=ROLE, blank=True, null=True)
    passport_number = CharField(max_length=9, blank=True, null=True)
    passport_give_date = DateField(blank=True, null=True)
    given_by_whom = CharField(max_length=255, blank=True, null=True)
    mfo = CharField(max_length=255, blank=True, null=True)
    r_s = CharField(max_length=255, blank=True, null=True)
    bank = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_letter_client_count(self):
        return self.letter_client.count()

    @property
    def get_letter_client(self):
        return self.letter_client.all()

    @property
    def get_letter_currier_count(self):
        return self.letter_currier.count()

    @property
    def get_letter_currier(self):
        return self.letter_currier.all()
