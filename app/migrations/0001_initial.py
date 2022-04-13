# Generated by Django 4.0.4 on 2022-04-11 19:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('inn', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.validate_integer])),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, choices=[('staff', 'Xodim'), ('client', 'Klient'), ('admin', 'Admin'), ('moderator', 'Moderator')], max_length=15, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=9, null=True)),
                ('passport_give_date', models.DateField(blank=True, null=True)),
                ('given_by_whom', models.CharField(blank=True, max_length=255, null=True)),
                ('mfo', models.CharField(blank=True, max_length=255, null=True)),
                ('r_s', models.CharField(blank=True, max_length=255, null=True)),
                ('bank', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Massive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='massive', to='app.district')),
            ],
            options={
                'verbose_name': 'Massiv',
                'verbose_name_plural': 'Massivlar',
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('new', 'yangi'), ('processing', 'yetkazilmoqda'), ('accepted', 'qabul qildi'), ('cancelled', 'qabul qilmadi')], default='new', max_length=20)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('barcode', models.CharField(blank=True, max_length=12, null=True)),
                ('letter_text', models.TextField(blank=True, null=True)),
                ('delivered_at', models.DateTimeField(blank=True, null=True)),
                ('curier_accepted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_client', to=settings.AUTH_USER_MODEL)),
                ('curier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_curier', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.region')),
            ],
            options={
                'verbose_name': 'Xat',
                'verbose_name_plural': 'Xatlar',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='app.region'),
        ),
        migrations.AddField(
            model_name='staff',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.district'),
        ),
        migrations.AddField(
            model_name='staff',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='staff',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region'),
        ),
        migrations.AddField(
            model_name='staff',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='BranchProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': 'Filiallar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.staff',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClientProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klientlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.staff',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ReportProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Xisobot',
                'verbose_name_plural': 'Xisobotlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.staff',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StaffProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Xodim',
                'verbose_name_plural': 'Xodimlar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.staff',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
