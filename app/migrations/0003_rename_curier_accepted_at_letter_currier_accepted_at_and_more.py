# Generated by Django 4.0.4 on 2022-05-04 18:32

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_staff_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='curier_accepted_at',
            new_name='currier_accepted_at',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='curier',
        ),
        migrations.AddField(
            model_name='letter',
            name='currier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_currier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='letter',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='letter/%Y/%m/%d', verbose_name='Fayl'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district', verbose_name='Tuman'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Xat'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.region', verbose_name='Viloyat'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Filial'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kompaniya'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district', verbose_name='Tuman'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='given_by_whom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kim tomonidan berilgan'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='inn',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.validate_integer], verbose_name='INN'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mfo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='MFO'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=255, verbose_name='FIO'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='passport_give_date',
            field=models.DateField(blank=True, null=True, verbose_name='Berilgan sana'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='passport_number',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Pasport seriyasi'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='r_s',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='R/s'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.region', verbose_name='Viloyat'),
        ),
    ]