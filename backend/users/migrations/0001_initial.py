# Generated by Django 4.2.1 on 2023-05-24 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')),
                ('role', models.CharField(choices=[('CANDIDATE', 'Кандидат'), ('INTERN', 'Стажер'), ('CURATOR', 'Куратор'), ('STAFF', 'Кадровый специалист'), ('MENTOR', 'Наставник')], default='CANDIDATE', max_length=16, verbose_name='Роль')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('surname', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='info', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthdate', models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения')),
                ('university_name', models.CharField(blank=True, max_length=50, verbose_name='Учебное заведение')),
                ('university_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Курс')),
                ('job_experience', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('skills', models.TextField(blank=True, verbose_name='Навыки')),
                ('departments', models.TextField(blank=True, verbose_name='Предпочитаемые направления стажировки')),
            ],
        ),
    ]
