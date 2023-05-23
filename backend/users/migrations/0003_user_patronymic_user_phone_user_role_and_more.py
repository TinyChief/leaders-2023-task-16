# Generated by Django 4.2.1 on 2023-05-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patronymic',
            field=models.CharField(default='', max_length=50, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CANDIDATE', 'Кандидат'), ('INTERN', 'Стажер'), ('CURATOR', 'Куратор'), ('STAFF', 'Кадровый специалист'), ('MENTOR', 'Наставник')], default='CANDIDATE', max_length=9, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]
